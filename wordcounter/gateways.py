import logging
from typing import Callable, Optional  # pylint: disable=unused-import

import google.cloud.exceptions
import google.cloud.storage

from config import config
from wordcounter.core.gateways import FileRepository as BaseFileRepository

logger = logging.getLogger(__name__)


class FileNotFoundException(Exception):
    """Raise when file was not found."""


def google_storage_file_loader(filepath: str) -> str:
    """Downloads a blob from a bucket as string."""
    logging.debug("Downloading %s from %s bucket", filepath, config["BUCKET_NAME"])
    storage_client = google.cloud.storage.Client.create_anonymous_client()
    try:
        bucket = storage_client.get_bucket(config["BUCKET_NAME"])
    except (google.cloud.exceptions.NotFound, ValueError) as e:
        raise FileNotFoundException(
            f"Can't reach bucket {config['BUCKET_NAME']}. Please, ensure that bucket exist and was public."
        ) from e
    blob = bucket.blob(filepath)
    if not blob.exists():
        msg = f"File `{filepath}` not found in bucket `{config['BUCKET_NAME']}`. "
        msg += "Please, ensure filename was correct and exists in bucket"
        raise FileNotFoundException(msg)
    return blob.download_as_string().decode("utf-8")


class FileRepository(BaseFileRepository):
    """
    Retrive text from a file.
    Loading file was done by loader function. This function introduces
    flexibility and allow load any file type and from any source.
    """

    def __init__(self, loader: Callable[[str], str], filepath: str):
        self._text = None  # type: Optional[str]
        self._filepath = filepath
        self._loader = loader

    @property
    def filepath(self) -> str:
        return self._filepath

    @property
    def text(self) -> str:
        """
        Method that make importing data a lazy function and wrap in a cache.
        In other does not load data until it is needed and ensures that
        it is only loaded once.
        """
        if not self._text:
            self._text = self._loader(self.filepath)
        return self._text

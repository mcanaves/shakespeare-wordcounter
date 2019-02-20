import csv
import logging
import os
from collections import Counter

from config import config
from wordcounter.core.reporters import FileReporter

logger = logging.getLogger(__name__)


class FileNotSupportedException(Exception):
    """Raise when file reported was not implemented."""


class CSVReporter(FileReporter):
    """Export results to a csv file"""

    def __init__(self, filename: str):
        _, file_extension = os.path.splitext(filename)
        if file_extension.lower() != self.extension:
            raise FileNotSupportedException(
                f"CSVReporter only supports `{self.extension}` files. Please, check filename has correct extension."
            )
        self.filename = filename

    @property
    def extension(self) -> str:
        return ".csv"

    def save(self, result: Counter):
        filepath = config["ROOT_DIR"].joinpath(self.filename)
        logger.debug("Saving result as csv on %s", filepath)
        with open(filepath, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["Word", "Counter"])
            for row in result.most_common():
                writer.writerow(row)

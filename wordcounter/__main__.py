import logging.config
from functools import partial

from config import config
from wordcounter.core.pipeline import wordcounter
from wordcounter.gateways import FileRepository, google_storage_file_loader
from wordcounter.reporters import CSVReporter

DEFAULT_BOOKS = [
    "shakespeare/kinglear.txt",
    "shakespeare/othello.txt",
    "shakespeare/romeoandjuliet.txt",
]

OUTPUT_FILE = "result.csv"


def main():
    logging.config.dictConfig(config["LOGGING"])
    repository = partial(FileRepository, google_storage_file_loader)
    wordcounter(CSVReporter(OUTPUT_FILE), *[repository(f) for f in DEFAULT_BOOKS])


if __name__ == "__main__":  # pragma: nocover
    main()

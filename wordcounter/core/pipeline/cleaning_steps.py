import logging
import string
from typing import Generator, Iterator

PUNCTUATION_TABLE = str.maketrans("", "", string.punctuation)

logger = logging.getLogger(__name__)


def filter_not_alphabetic(tokens: Iterator[str]) -> Generator[str, None, None]:
    """Remove tokens that not are words"""
    for token in tokens:
        if token.isalpha():
            yield token


def remove_punctuation(tokens: Iterator[str]) -> Generator[str, None, None]:
    """
    Clean tokens to keep it without the punctuation like commas and quotes.
    We also want to keep contractions together.
    """
    for token in tokens:
        yield token.translate(PUNCTUATION_TABLE)


def to_lowercase(tokens: Iterator[str]) -> Generator[str, None, None]:
    """
    Convert all the words into a single case to facilitate comparison
    between them.
    """
    for token in tokens:
        yield token.lower()

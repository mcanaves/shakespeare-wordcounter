import logging
from collections import Counter
from typing import List

from wordcounter.core.gateways import FileRepository
from wordcounter.core.pipeline.cleaning_steps import (
    filter_not_alphabetic,
    remove_punctuation,
    to_lowercase,
)
from wordcounter.core.pipeline.utils import pipeline_composer

logger = logging.getLogger(__name__)


def token_loader(repository: FileRepository) -> List[str]:
    """Split text into tokens"""
    logging.debug("Loading %s", repository.filepath)
    text = repository.text
    return text.split()


def token_cleaner(tokens: List[str]) -> List[str]:
    """Cleaning pipeline"""
    logging.debug("Cleaning %s tokens", len(tokens))
    cleaning_pipeline = pipeline_composer(
        remove_punctuation, filter_not_alphabetic, to_lowercase
    )
    return list(cleaning_pipeline(tokens))


def word_counter(words: List[str]) -> Counter:
    """Count words using python's high performance Counter collection"""
    logging.debug("Counting %s words", len(words))
    return Counter(words)

import logging
import os
from collections import Counter
from typing import List

from wordcounter.core.gateways import FileRepository
from wordcounter.core.pipeline.main_steps import (
    token_cleaner,
    token_loader,
    word_counter,
)
from wordcounter.core.pipeline.utils import pipeline_composer
from wordcounter.core.reporters import FileReporter

logger = logging.getLogger(__name__)


def wordcounter(reporter: FileReporter, *repositories: FileRepository):
    """Word counter main pipeline"""
    logger.info("Starting word counter...")
    count_pipeline = pipeline_composer(token_loader, token_cleaner, word_counter)
    result = sum([count_pipeline(r) for r in repositories], Counter())
    reporter.save(result)

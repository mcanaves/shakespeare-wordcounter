"""
Contracts that acts as boundary between app core and presenter layer.
"""

from collections import Counter


class FileReporter:
    """Export results to a file"""

    @property
    def extension(self) -> str:
        raise NotImplementedError

    def save(self, result: Counter):
        raise NotImplementedError

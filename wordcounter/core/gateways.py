"""
Contracts that acts as boundary between app core and data providers layer.
"""


class FileRepository:
    """Retrive text from a file"""

    @property
    def filepath(self) -> str:
        raise NotImplementedError

    @property
    def text(self) -> str:
        raise NotImplementedError

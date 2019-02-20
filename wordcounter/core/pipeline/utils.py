from functools import reduce
from typing import Any, Callable


def pipeline_composer(*steps: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    Utility to chain generator functions using left fold aproach
    """
    return lambda x: reduce(lambda f, g: g(f), list(steps), x)

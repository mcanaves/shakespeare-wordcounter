import pytest

from wordcounter.core.pipeline.main_steps import (
    token_cleaner,
    token_loader,
    word_counter,
)


def test_loader(mocker):
    repository_mock = mocker.Mock(text="Hola a todos!")
    assert token_loader(repository_mock) == ["Hola", "a", "todos!"]


def test_loader_file_not_found():
    with pytest.raises(Exception):
        assert token_loader("test_data.txt")


def test_cleaner():
    cleaned_words = token_cleaner(["Hi,", "my", "name", "is", "MATEU!"])
    assert cleaned_words == ["hi", "my", "name", "is", "mateu"]


def test_counter():
    counted_words = word_counter(["a", "a", "b", "a", "c"])
    assert counted_words == {"a": 3, "b": 1, "c": 1}

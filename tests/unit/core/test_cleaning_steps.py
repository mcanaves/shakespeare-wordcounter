from wordcounter.core.pipeline.cleaning_steps import (
    filter_not_alphabetic,
    remove_punctuation,
    to_lowercase,
)


def test_remove_punctuation():
    dirty_words = ["test", "test!", "test.", "test's", "another-test"]
    assert {"test", "tests", "anothertest"} == set(remove_punctuation(dirty_words))


def test_filter_not_alphabetic():
    tokens = [",", "!", "test", "..."]
    assert ["test"] == list(filter_not_alphabetic(tokens))


def test_to_lowercase():
    tokens = ["TEST", "Test", "test"]
    assert {"test"} == set(to_lowercase(tokens))

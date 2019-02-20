import pytest

from wordcounter.reporters import CSVReporter, FileNotSupportedException


@pytest.mark.parametrize("filename", [("test"), ("test.txt"), ("/path/test.txt")])
def test_csv_reporter_bad_extension(filename):
    with pytest.raises(FileNotSupportedException):
        CSVReporter(filename=filename)


def test_csv_reporter_extension():
    reporter = CSVReporter("test.csv")
    assert reporter.extension == ".csv"


def test_csv_reporter_save():
    reporter = CSVReporter("test.csv")
    assert reporter.extension == ".csv"

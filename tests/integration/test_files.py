from collections import Counter

from config import config
from wordcounter.reporters import CSVReporter


def test_save_csv():
    result = Counter("test")
    file = config["ROOT_DIR"].joinpath("test.csv")
    CSVReporter("test.csv").save(result)
    assert file.is_file()
    assert file.read_bytes() == b"Word,Counter\r\nt,2\r\ne,1\r\ns,1\r\n"
    file.unlink()

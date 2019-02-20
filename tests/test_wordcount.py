from config import config
from wordcounter.__main__ import main


def test_wordcount(mocker):
    mocker.patch("wordcounter.__main__.OUTPUT_FILE", "test.csv")
    result_file = config["ROOT_DIR"].joinpath("test.csv")
    main()
    assert result_file.is_file()
    result_file.unlink()

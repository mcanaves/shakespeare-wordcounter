from wordcounter.gateways import FileRepository


def test_file_repository_filepath(mocker):
    repository = FileRepository(mocker.Mock(), "file/path/test.text")
    assert repository.filepath == "file/path/test.text"


def test_file_repository_text(mocker):
    loader_mock = mocker.Mock(return_value="test")
    repository = FileRepository(loader_mock, "file/path/test.text")
    assert repository.text == "test"
    assert repository.text == "test"
    loader_mock.assert_called_once_with("file/path/test.text")

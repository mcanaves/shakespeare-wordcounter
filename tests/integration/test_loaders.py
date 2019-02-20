import pytest

from wordcounter.gateways import FileNotFoundException, google_storage_file_loader


def test_google_loader():
    text = google_storage_file_loader("shakespeare/kinglear.txt")
    assert len(text) == 157_283
    assert "KING LEAR" in text


def test_google_loader_bucket_not_found(mocker):
    mocker.patch.dict(
        "wordcounter.gateways.config", {"BUCKET_NAME": "bucketnamethatnoexist"}
    )
    with pytest.raises(FileNotFoundException):
        google_storage_file_loader("shakespeare/kinglear.txt")


def test_google_loader_bucket_bad_permisions(mocker):
    mocker.patch.dict("wordcounter.gateways.config", {"BUCKET_NAME": "bad"})
    with pytest.raises(FileNotFoundException):
        google_storage_file_loader("shakespeare/kinglear.txt")


def test_google_loader_blob_not_exists():
    with pytest.raises(FileNotFoundException):
        google_storage_file_loader("shakespeare/bad.txt")

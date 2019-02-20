from wordcounter.core.pipeline import wordcounter


def test_wordcounter(mocker):
    test_text1 = "Hola a todos!"
    test_text2 = """
    Hola a todos de nuevo!

    Un saludo,
    @mcanaves
    """
    repository_mock1 = mocker.Mock(text=test_text1)
    repository_mock2 = mocker.Mock(text=test_text2)
    reporter_mock = mocker.Mock()
    wordcounter(reporter_mock, repository_mock1, repository_mock2)
    reporter_mock.save.assert_called_once_with(
        {
            "a": 2,
            "de": 1,
            "hola": 2,
            "nuevo": 1,
            "todos": 2,
            "un": 1,
            "saludo": 1,
            "mcanaves": 1,
        }
    )

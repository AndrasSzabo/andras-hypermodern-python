import click
import click.testing
import pytest
import requests


from andras_hypermodern_python import console


@pytest.fixture
def mock_wikipedia_random_page(mocker):
    return mocker.patch("andras_hypermodern_python.wikipedia.random_page")


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_uses_specified_language(runner, mock_wikipedia_random_page):
    # test that the random_page function is called with the specified language
    runner.invoke(console.main, ["--language=pl"])
    mock_wikipedia_random_page.assert_called_with(language="pl")


def test_main_succeeds(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert "Lorem Ipsum, title!" in result.output


def test_main_invokes_requests_get(runner, mock_requests_get):
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_uses_en_wikipedia_org(runner, mock_requests_get):
    runner.invoke(console.main)
    # Get the arguments that were passed to the mocked function:
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]


def test_main_fails_on_request_error(runner, mock_requests_get):
    # mock to raise an exception instead of returning a value:
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_message_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = requests.RequestException
    # The above exception comes form the requests package
    result = runner.invoke(console.main)
    assert "Error" in result.output
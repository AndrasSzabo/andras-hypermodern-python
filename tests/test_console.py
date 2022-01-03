"""Test cases for the console module."""
from unittest.mock import Mock

import click
import click.testing
from click.testing import CliRunner
import pytest
from pytest_mock import MockFixture
import requests


from andras_hypermodern_python import console


@pytest.fixture
def mock_wikipedia_random_page(mocker: MockFixture) -> Mock:
    """Fixture for mocking wikipedia.random_page."""
    return mocker.patch("andras_hypermodern_python.wikipedia.random_page")


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return click.testing.CliRunner()


def test_main_uses_specified_language(
    runner: CliRunner, mock_wikipedia_random_page: Mock
) -> None:
    """It uses the specified language edition of Wikipedia."""
    runner.invoke(console.main, ["--language=pl"])
    mock_wikipedia_random_page.assert_called_with(language="pl")


def test_main_succeeds(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It exits with a status code of zero (end-to-end)."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It prints the title of the Wikipedia page."""
    result = runner.invoke(console.main)
    assert "Lorem Ipsum, title!" in result.output


def test_main_invokes_requests_get(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It invokes requests.get."""
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_uses_en_wikipedia_org(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It uses the English Wikipedia by default."""
    runner.invoke(console.main)
    # Get the arguments that were passed to the mocked function:
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]


def test_main_fails_on_request_error(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    """It exits with a non-zero exit status code if the request fails."""
    # mock to raise an exception instead of returning a value:
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_message_on_request_error(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    """It prints an error message if the request fails."""
    mock_requests_get.side_effect = requests.RequestException
    # The above exception comes form the requests package
    result = runner.invoke(console.main)
    assert "Error" in result.output

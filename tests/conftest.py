from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture

# The file conftest.py is automatically available for all test files in this dir


@pytest.fixture
def mock_requests_get(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    # The following is how the response json data is returned by the requests package.
    # (it seems quite complicated, the article looks under the hood for this chain-call)
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum, title!",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock

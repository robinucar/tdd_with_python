import pytest
from pytest import raises
from unittest.mock import MagicMock
from lib.LineReader import readFromFile


@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr('builtins.open', mock_open)
    return mock_open
# readFromFile returns correct string using MagicMock


def test_returnsCorrectString(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    result = readFromFile("python")
    mock_open.assert_called_once_with("python", "r")
    assert result == "test line"


# readFromFile throws exception when file does not exist
def test_throwsExceptionWithNonExistFile(monkeypatch):
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with raises(Exception):
        result = readFromFile("Java")

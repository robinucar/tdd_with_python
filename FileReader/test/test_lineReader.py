import pytest
from unittest.mock import MagicMock
from lib.LineReader import readFromFile

# Call readFromFile


# readFromFile returns correct string usin MagicMock
def test_returnsCorrectString(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr('builtins.open', mock_open)
    result = readFromFile("python")
    mock_open.assert_called_once_with("python", "r")
    assert result == "test line"
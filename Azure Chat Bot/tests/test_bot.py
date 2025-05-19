import pytest
from src.bot.helpers import format_response, validate_input

def test_format_response():
    message = "Hello"
    formatted = format_response(message)
    assert formatted == "🤖 Hello"

def test_validate_input():
    assert validate_input("Hello") is True
    assert validate_input("   ") is False
    assert validate_input("") is False

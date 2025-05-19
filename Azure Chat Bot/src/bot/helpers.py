import logging

# Set up structured logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def format_response(message: str) -> str:
    """
    Formats bot responses consistently.

    Args:
        message (str): The message to format.

    Returns:
        str: The formatted response string.
    """
    logger.debug(f"Formatting response: {message}")
    return f"🤖 {message}"


def validate_input(user_input: str) -> bool:
    """
    Validates user input (simple placeholder logic).

    Args:
        user_input (str): The user input text.

    Returns:
        bool: True if input is valid, False otherwise.
    """
    logger.debug(f"Validating input: {user_input}")
    return bool(user_input and len(user_input.strip()) > 0)

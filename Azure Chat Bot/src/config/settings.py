import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Settings:
    """Environment-based settings loader."""

    def __init__(self):
        self.app_id = os.getenv("MicrosoftAppId", "")
        self.app_password = os.getenv("MicrosoftAppPassword", "")
        self.environment = os.getenv("ENVIRONMENT", "development")
        logger.info(f"Settings loaded: ENVIRONMENT={self.environment}")

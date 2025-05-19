import logging
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ExternalAPIService:
    """Handles interactions with external APIs."""

    def __init__(self, base_url):
        self.base_url = base_url
        logger.info(f"ExternalAPIService initialized with base URL: {self.base_url}")

    def fetch_data(self, endpoint: str):
        try:
            url = f"{self.base_url}/{endpoint}"
            logger.info(f"Fetching data from: {url}")
            response = requests.get(url)
            response.raise_for_status()
            logger.info("Data fetched successfully.")
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching data: {e}")
            return None

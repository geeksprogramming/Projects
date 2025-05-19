import os
import logging
from cryptography.fernet import Fernet

# Set up structured logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class EncryptionUtil:
    """
    Utility class for encrypting and decrypting sensitive data
    using Fernet symmetric encryption.
    """

    def __init__(self, key: str = None):
        """
        Initialize EncryptionUtil with a provided key or environment variable.
        """
        self.key = key or os.getenv("ENCRYPTION_KEY")
        if not self.key:
            raise ValueError("Encryption key not found. Set ENCRYPTION_KEY in environment variables.")
        
        self.fernet = Fernet(self.key)
        logger.info("EncryptionUtil initialized successfully.")

    def encrypt(self, data: str) -> str:
        """
        Encrypts the given data string.
        Args:
            data (str): Plain text data to encrypt.
        Returns:
            str: Encrypted string.
        """
        logger.debug("Encrypting data.")
        encrypted_data = self.fernet.encrypt(data.encode())
        return encrypted_data.decode()

    def decrypt(self, token: str) -> str:
        """
        Decrypts the given token string.
        Args:
            token (str): Encrypted token to decrypt.
        Returns:
            str: Decrypted plain text.
        """
        logger.debug("Decrypting data.")
        decrypted_data = self.fernet.decrypt(token.encode())
        return decrypted_data.decode()

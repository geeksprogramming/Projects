# Azure Chatbot App (Enterprise Ready)

This is an enterprise-ready Azure Web App Chatbot built with the Bot Framework SDK for Python.

## 📂 Project Structure

```plaintext
src/
  bot/
    main_bot.py         # Main bot logic
    startup.py          # Adapter, state setup
    helpers.py          # Utility functions
  dialogs/
    welcome_dialog.py   # Handles welcome flow
    faq_dialog.py       # Handles FAQ flow
  config/
    settings.py         # Environment settings
  services/
    external_api_service.py  # External API integration
tests/
deployment/
  docker/
    Dockerfile
    runtime.txt
  templates/
    azuredeploy.json

requirements.txt
azure-pipelines.yml

## 🔐 Encryption Key Setup (Optional)

If your chatbot handles sensitive information (like secrets, tokens, or personal data), you can enable encryption using the Python cryptography module.

Steps to do this - 

1. Add Cryptography in requirements.txt

2. Generate an Encryption Key
    Run this once in Python:

from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())

Copy the generated key and store it securely.

3. Create or Update .env File
ENCRYPTION_KEY=your-generated-key-here

❗ Do not commit this file to GitHub. It’s ignored via .gitignore.

4. Use the Key in Code
Use the following in your service:

from src.services.encryption_util import EncryptionUtil

crypto = EncryptionUtil()
token = crypto.encrypt("my-secret")
original = crypto.decrypt(token)

In production (e.g., Azure App Service), configure ENCRYPTION_KEY in the App Settings or Key Vault securely.

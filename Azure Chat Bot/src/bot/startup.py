import logging
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    BotFrameworkAdapter,
    MemoryStorage,
    ConversationState,
    UserState,
)
from src.bot.main_bot import MainBot
from src.dialogs.welcome_dialog import WelcomeDialog

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def create_adapter(app_id: str, app_password: str) -> BotFrameworkAdapter:
    settings = BotFrameworkAdapterSettings(app_id, app_password)
    adapter = BotFrameworkAdapter(settings)

    async def on_error(context, error: Exception):
        logger.error(f"Bot error: {error}")
        await context.send_activity("⚠️ Sorry, something went wrong.")

    adapter.on_turn_error = on_error
    logger.info("Adapter created.")
    return adapter

def create_conversation_user_state():
    storage = MemoryStorage()
    conversation_state = ConversationState(storage)
    user_state = UserState(storage)
    logger.info("State initialized.")
    return conversation_state, user_state

def create_bot(conversation_state: ConversationState, user_state: UserState) -> MainBot:
    dialog = WelcomeDialog(user_state)
    return MainBot(conversation_state, user_state, dialog)

import logging
from botbuilder.core import ActivityHandler, TurnContext, ConversationState, UserState
from botbuilder.schema import ChannelAccount
from src.dialogs.welcome_dialog import WelcomeDialog

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class MainBot(ActivityHandler):
    def __init__(self, conversation_state: ConversationState, user_state: UserState, dialog: WelcomeDialog):
        if not conversation_state:
            raise ValueError("Missing conversation_state")
        if not user_state:
            raise ValueError("Missing user_state")
        if not dialog:
            raise ValueError("Missing dialog")

        self.conversation_state = conversation_state
        self.user_state = user_state
        self.dialog = dialog
        self.dialog_state_accessor = self.conversation_state.create_property("DialogState")
        logger.info("MainBot initialized.")

    async def on_members_added_activity(self, members_added: [ChannelAccount], turn_context: TurnContext):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                logger.info(f"New member added: {member.name}")
                await turn_context.send_activity("👋 Hi! I'm your Azure ChatBot. How can I help you today?")
                await self.dialog.begin_dialog(turn_context, self.dialog_state_accessor)

    async def on_message_activity(self, turn_context: TurnContext):
        logger.info(f"User message: {turn_context.activity.text}")
        await self.dialog.run(turn_context, self.dialog_state_accessor)

    async def on_turn(self, turn_context: TurnContext):
        await super().on_turn(turn_context)
        await self.conversation_state.save_changes(turn_context)
        await self.user_state.save_changes(turn_context)
        logger.debug("State changes saved.")

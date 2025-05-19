import logging
from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext
from botbuilder.dialogs.prompts import TextPrompt, PromptOptions
from botbuilder.core import MessageFactory
from src.bot.helpers import format_response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class WelcomeDialog(ComponentDialog):
    def __init__(self, user_state):
        super(WelcomeDialog, self).__init__(WelcomeDialog.__name__)

        self.add_dialog(TextPrompt("TextPrompt"))
        self.add_dialog(
            WaterfallDialog("MainWaterfall", [self.prompt_for_name, self.acknowledge_user])
        )

        self.initial_dialog_id = "MainWaterfall"

    async def prompt_for_name(self, step_context: WaterfallStepContext):
        logger.info("Prompting user for their name.")
        prompt_message = MessageFactory.text("May I know your name?")
        return await step_context.prompt("TextPrompt", PromptOptions(prompt=prompt_message))

    async def acknowledge_user(self, step_context: WaterfallStepContext):
        user_name = step_context.result
        logger.info(f"Received user name: {user_name}")
        response = format_response(f"Nice to meet you, {user_name}! How can I assist you today?")
        await step_context.context.send_activity(response)
        return await step_context.end_dialog()

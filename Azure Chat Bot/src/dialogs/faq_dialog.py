import logging
from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext
from botbuilder.dialogs.prompts import TextPrompt, PromptOptions
from botbuilder.core import MessageFactory
from src.bot.helpers import format_response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class FAQDialog(ComponentDialog):
    def __init__(self, user_state):
        super(FAQDialog, self).__init__(FAQDialog.__name__)

        self.add_dialog(TextPrompt("TextPrompt"))
        self.add_dialog(
            WaterfallDialog("FAQWaterfall", [self.ask_question, self.answer_question])
        )

        self.initial_dialog_id = "FAQWaterfall"

    async def ask_question(self, step_context: WaterfallStepContext):
        logger.info("Asking user for FAQ question.")
        prompt_message = MessageFactory.text("What question do you have?")
        return await step_context.prompt("TextPrompt", PromptOptions(prompt=prompt_message))

    async def answer_question(self, step_context: WaterfallStepContext):
        question = step_context.result
        logger.info(f"Received FAQ question: {question}")
        # Placeholder response logic
        response = format_response("That's a great question! Here's a helpful answer.")
        await step_context.context.send_activity(response)
        return await step_context.end_dialog()

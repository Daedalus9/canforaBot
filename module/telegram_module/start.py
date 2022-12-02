from var.text import WELCOME_MESSAGE


def start(update, context):
    chat_id=update.effective_chat.id
    context.bot.send_message(chat_id, WELCOME_MESSAGE)
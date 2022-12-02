from telegram.ext import CommandHandler
from module.telegram_module.start import start

def cHandlers(updater):
    dispatcher=updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
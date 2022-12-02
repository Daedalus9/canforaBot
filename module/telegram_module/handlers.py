from telegram.ext import CommandHandler
from module.telegram_module.start import start
from module.telegram_module.get_admin import get_admin

def cHandlers(updater):
    dispatcher=updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('getadmin', get_admin))
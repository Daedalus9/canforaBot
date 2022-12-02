from telegram.ext import CommandHandler
from module.telegram_module.start import start
from module.telegram_module.get_admin import get_admin
from module.telegram_module.request_admin import request_admin
from module.telegram_module.addadmin import add_admin
from module.telegram_module.getuser import getuser
from module.telegram_module.requestuser import requestuser
from module.telegram_module.adduser import adduser
from module.telegram_module.bacheca import bacheca
from module.telegram_module.addbacheca import addbacheca

def cHandlers(updater):
    dispatcher=updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('getadmin', get_admin))
    dispatcher.add_handler(CommandHandler('requestadmin', request_admin))
    dispatcher.add_handler(CommandHandler('addadmin', add_admin))
    dispatcher.add_handler(CommandHandler('getuser', getuser))
    dispatcher.add_handler(CommandHandler('requestuser', requestuser))
    dispatcher.add_handler(CommandHandler('adduser', adduser))
    dispatcher.add_handler(CommandHandler('bacheca', bacheca))
    dispatcher.add_handler(CommandHandler('addbacheca', addbacheca))
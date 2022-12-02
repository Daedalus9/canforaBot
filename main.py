import yaml
import logging
from telegram.ext import Updater
from module.telegram_module.handlers import cHandlers

def main():
    with open(r"./var/telegram_token.yaml") as file:
        data = yaml.full_load(file)
        TOKEN = data['token']
        updater= Updater(TOKEN, use_context=True)
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        cHandlers(updater)
        updater.start_polling()
        updater.idle()

if __name__ == '__main__':
    main()

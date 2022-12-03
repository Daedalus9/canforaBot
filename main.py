import yaml
import logging
from datetime import time
from telegram.ext import Updater
from module.telegram_module.handlers import cHandlers
from module.telegram_module.waste_sorting import waste_sorting

def main():
    with open(r"./var/telegram_token.yaml") as file:
        data = yaml.full_load(file)
        TOKEN = data['token']
        updater= Updater(TOKEN, use_context=True)
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        cHandlers(updater)
        j = updater.job_queue
        a=time(19,30,00)
        job_minute = j.run_daily(waste_sorting, a)
        updater.start_polling()
        updater.idle()

if __name__ == '__main__':
    main()

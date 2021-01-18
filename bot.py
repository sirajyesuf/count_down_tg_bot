import logging
from telegram import Update
from telegram.ext import Updater

import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('token')



# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
#handlers
from handlers.cmd import start_cmd_handler
from handlers.btn import add_btn_conv_handler,timezone_btn_handler
from handlers.callback_query import callback_query_handler


def main():
    updater = Updater(token=token,use_context=True)
    dispatcher = updater.dispatcher
    #add handlers
    dispatcher.add_handler(start_cmd_handler)
    dispatcher.add_handler(add_btn_conv_handler)
    dispatcher.add_handler(timezone_btn_handler)
    dispatcher.add_handler(callback_query_handler)
    
    #start the bot
    updater.start_polling()
    #until you press ctrl-c
    updater.idle()


if __name__ == '__main__':
    main()
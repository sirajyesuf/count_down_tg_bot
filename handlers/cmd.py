from telegram.ext import CallbackContext,MessageHandler,CommandHandler
from telegram import Update

from btns import main_menu
def start(update:Update,context:CallbackContext)->None:
    update.message.reply_text("Hi !")
    context.bot.send_message(
        chat_id = update.effective_user.id,
        text = "HI!",
        reply_markup = main_menu
        
    )



start_cmd_handler = CommandHandler('start',start)


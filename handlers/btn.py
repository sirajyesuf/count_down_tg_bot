from telegram import Update
from telegram.ext import CallbackContext,Filters,ConversationHandler,MessageHandler,CommandHandler
from datetime import datetime
from custome_filters import DatetimeFilter
from db import Timezone
from validators import future_datetime
from btns import chooses,add_to
START_ADD,DATE_TIME,GAP,TO = range(4)


    
def xxxx(update,context,index):
    msg=""
    if index==1:
        msg = "Enter the End Date  in the format of YYYY-MM-DD HH:MM:SS eg 2021-01-29 09:45:34 \n\n use /cancel to terminate the process"

        context.bot.send_message(
            chat_id = update.effective_user.id,
            text = msg
        )

    if index==2:
        msg = "pls select one of the following"
        context.bot.send_message(
            chat_id = update.effective_user.id,
            text = msg,
            reply_markup = chooses
        )
    if index==3:
        msg="pls select"
        context.bot.send_message(
            chat_id = update.effective_user.id,
            text = msg,
            reply_markup = add_to()
        )




@future_datetime
def date_time(update:Update,context:CallbackContext)->int:
    # print(context.user_data["add_cdt"])
    cdt = datetime.fromisoformat(update.message.text)
    context.user_data["add_cdt"]["endtime"] = cdt
    # print(context.user_data['add_cdt'])
    xxxx(update,context,2)
    return GAP

def gap(update:Update,context:CallbackContext)->int:
    pass

def to(update:Update,context:CallbackContext)->int:
    pass

def start_add(update:Update,context:CallbackContext)->int:
    context.user_data["add_cdt"] = {}
    xxxx(update,context,1)

   
    return DATE_TIME
def cancel(update:Update,context:CallbackContext)->str:
    context.bot.send_message(
        chat_id = update.effective_user.id,
        text = "canceled"
    )
    return ConversationHandler.END




main_menu1 = ['➕Add']

add_btn_conv_handler = ConversationHandler(
    entry_points = [MessageHandler(Filters.text(main_menu1),start_add)],
    states = {
        DATE_TIME :[MessageHandler(DatetimeFilter(),date_time)],
    },
    fallbacks = [CommandHandler('cancel',cancel)]






)






def timezone(update:Update,context:CallbackContext)->str:
    timezone_info_user = Timezone().get_user_timezone_info(13457890)
    msg = "no time zone for u"
    if timezone_info_user:
        msg = "👤\n\n{}".format(timezone_info_user["timezone"])

    print("timezones......👤")
    context.bot.send_message(
        chat_id  = update.effective_user.id,
        text = msg
    )


main_menu2=['🕙TimeZone']
timezone_btn_handler = MessageHandler(Filters.text(main_menu2),timezone)
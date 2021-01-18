import datetime
from telegram import Update
from telegram.ext import CallbackContext

def future_datetime(func):
    """
    the date time must be in the future 
    """
    def wrapper(update:Update,context:CallbackContext):
        if datetime.datetime.fromisoformat(update.message.text) > datetime.datetime.today():
            func(update,context)
        else:
            context.bot.send_message(
                chat_id = update.effective_user.id,
                text = "we can not back to the past pls enter future time"
            )
    return wrapper
    


# def  xx(func):
#     def wrapper(a,b,**kwargs):
#         print(kwargs)
#         print(a,b)
#         func(a,b)
#     return wrapper

# @xx
# def zz(a,b,**kwargss):
#     print("zz",a,b)


# zz(1,2,c=999)
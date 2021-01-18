from telegram import ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton
from telegram.utils import helpers
main_menu = ReplyKeyboardMarkup( [
    ['➕Add','🕙TimeZone']
],resize_keyboard=True)


chooses = InlineKeyboardMarkup([

[
InlineKeyboardButton(text="hourly",callback_data="3600"),
InlineKeyboardButton(text="daily",callback_data="24800"),
InlineKeyboardButton(text="minutely",callback_data="60"),
InlineKeyboardButton(text="10secondly",callback_data="10")
]



])

def add_to(update,context):
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.get_me().username,"unique token here",group=True)
    return InlineKeyboardMarkup([
        [
        InlineKeyboardButton(text="only for me",callback_data="me"),
        InlineKeyboardButton(text="add to telegram group",url=url),
        ]
    ])
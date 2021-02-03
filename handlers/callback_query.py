from telegram.ext import CallbackContext,CallbackQueryHandler
from telegram import Update
from .btn import xxxx
# 3600
# 24800
# 60
# 10

def callback_query(update:Update,context:CallbackContext):
    query  = update.callback_query
    # print(query.data)
    if query.data == str(10):
        # print("query")
        context.user_data["add_cdt"]["gap"] = query.data
        query.delete_message()
        # print(context.user_data["add_cdt"])
        xxxx(update,context,3)

    
    if query.data == "me":
        context.user_data["add_cdt"]["to"] = update.effective_user.id
        query.delete_message()






















callback_query_handler = CallbackQueryHandler(callback_query)




# mongodb+srv://<username>:<password>@cluster0.moppb.mongodb.net/<dbname>?retryWrites=true&w=majority
from telegram.ext import MessageFilter
import datetime
class DatetimeFilter(MessageFilter):
    def filter(self,message):
        try:
            datetime.datetime.fromisoformat(message.text)
            print("accepted")
            return True
        except ValueError:
            print("rejected")
            return False
        


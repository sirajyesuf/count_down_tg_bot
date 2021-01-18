import pymongo
import datetime
client = pymongo.MongoClient()
db = client['count_down_bot']
# users = db['users']
# timezones = db['timezones']
# user = {
#     'name' :'siraj',
#     'age' :22,
#     'bday':datetime.datetime.now()
# }
# timezone1 = {
#     'user_id':389387515,
#     'timezone':'Africa/Addis_Ababa'
# }

# u1 = users.insert_one(user).inserted_id
# t1=timezones.insert_one(timezone1)
# print(u1)
# print(users.find_one())
# print(users.find())
# for i in users.find():
#     print(i)
# print(timezones.find())
# for tz in timezones.find():
#     print(tz)


# dt = datetime.datetime.today()
# tp = dt.replace(tzinfo = datetime.timezone.utc)
# print(tp)

# from datetime import datetime
# import pytz

# utc = pytz.utc
# IST = pytz.timezone('Asia/Kolkata')
# EAT = pytz.timezone('Africa/Addis_Ababa')
# print("utc:",datetime.now(utc))
# print("ist:",datetime.now(EAT))




class Timezone():

    def get_user_timezone_info(self,user_id):
        timezones = db['timezones']
        client.close()
        for tz in timezones.find():
            if tz['user_id'] == int(user_id):
                return tz



# Timezone().get_user_timezone_info(389387515)

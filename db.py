
import os
from dotenv import load_dotenv
load_dotenv()


import pymongo
import datetime


class DB:
    client = None
    collection = None
    def __init__(self):
        DB.client = pymongo.MongoClient()
        DB.collection = self.client[os.getenv('db')]
          
    
# db1 = DB()
# print(DB.collection,DB.client)




class Model(DB):

    def __init__(self,tbl):
        DB.__init__(self)
        self.tbl = self.collection[tbl] 
       
    def create(self,data):
        if self.tbl.insert_one(data):
            return 1
        else:
            return 0
    def all(self):
        return self.tbl.find()
    
    def find(self,whr):
        return self.tbl.find_one(whr)
    def delete(self,whr):
        return self.tbl.delete_one(whr)
    def update(self,whr,new_val):
        return self.tbl.update_one(whr,new_val)





    


# model = Model("users")

# print(model.client,model.collection)



class User(Model):
    def __init__(self):
        Model.__init__(self,'users')


class Note(Model):
    def __init__(self):
        Model.__init__(self,'notes')


# user = User()
# u1= {
#     'name' :'xxx',
#     'age' :22,
#     'bday':datetime.datetime.now()
# }
# print(user.tbl)
# print(user.create(u1))



# for i in user.tbl.find():
#     print(i)


note = Note()
note1 = {
    'title' : "laravel advanced",
    'completed':0

}
# id =[]
# print(note.create(note1))
# for i in note.all():
#     print(i)
#     id.append(i['_id'])
# print(id)

# idx = [ObjectId('6019f2295e30f905b6173c1d'), ObjectId('6019f58b4e46e56091e50d63'), ObjectId('6019f5a0453273f914c6e20c'), ObjectId('6019f5b3c097b9c46f2ba9ea'), ObjectId('6019f5e37342f1bb28164c8c'), ObjectId('6019f5ffcac275ac8ba7c7aa')]

# for i in idx:

#     print(note.find())


print(note.find({'title':'laravel advanced'}))
# print(note.delete({'title':'laravel advanced'}))
# print(note.find({'title':'laravel advanced'}))

#update
whr = {'title':'laravel advanced'}
newval = { "$set": { "title": "django3" } }
print(note.update(whr,newval))
for i in note.all():
    print(i)





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




# class Timezone():

#     def get_user_timezone_info(self,user_id):
#         timezones = db['timezones']
#         client.close()
#         for tz in timezones.find():
#             if tz['user_id'] == int(user_id):
#                 return tz



# Timezone().get_user_timezone_info(389387515)

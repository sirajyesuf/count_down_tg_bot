from db import DB

class Model(DB):

    def __init__(self,tbl):
        DB.__init__(self)
        self.tbl = self.collection[tbl] 
       
    def create(self,data):
        return self.tbl.insert_one(data)

    def all(self):
        return self.tbl.find()
    
    def find(self,whr):
        return self.tbl.find_one(whr)

    def delete(self,whr):
        return self.tbl.delete_one(whr)

    def update(self,whr,new_val):
        return self.tbl.update_one(whr,new_val)


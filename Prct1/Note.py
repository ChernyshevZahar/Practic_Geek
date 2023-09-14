import datetime  



  
class Note:  
    def __init__(self, id, title, content):  
        self.id = id  
        self.title = title  
        self.content = content  
        self.created_at = datetime.datetime.now()  
        self.updated_at = datetime.datetime.now()  
  
    def update(self, title, content):  
        self.title = title  
        self.content = content  
        self.updated_at = datetime.datetime.now()  
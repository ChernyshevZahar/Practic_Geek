import datetime  



  
class Note:  
    def __init__(self, id, title, content):
        """  
        Создает класс для записи 
    
        Args:  
            id - id записи,
            title - заголовок записи,
            content - текст записи , 
    
        Returns:  
            Объект запись  
        """   
        self.id = id  
        self.title = title  
        self.content = content  
        self.created_at = datetime.datetime.now()  
        self.updated_at = datetime.datetime.now()  
  
    def update(self, title, content): 
        """  
        Создает класс для обновления записи 
    
        Args:  
            
            title - заголовок записи,
            content - текст записи,  
    
        Returns:  
            Обновленую запись  
        """ 
        self.title = title  
        self.content = content  
        self.updated_at = datetime.datetime.now()  
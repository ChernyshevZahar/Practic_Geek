import os
from Note import *
import json  




class NotesManager:  
    def __init__(self, name="nodes"):
        """  
        Создает класс для блокнота 
    
        Args:  
            name - имя для создания файла json  
    
        Returns:  
            Объект Блокнот  
        """  
        self.name = f'{name}.json'  
        self.notes = []
        if(os.path.exists(self.name)):
            self.note_id = self.info_note_last_id(filename=self.name)
        else:  
            self.note_id = 0 
        self.load_notes()

    def info_note_last_id(self,filename):
        try:  
            with open(filename, 'r') as file:  
                notes_data = json.load(file)
                if(len(notes_data)>0):
                    return int(notes_data[-1]['id'])
                else:
                    return 0        
        except FileNotFoundError as e:
            return False 
  
    def create_note(self, title, content):
        """  
        Создает запись в блокноте 
    
        Args:
            title - заголовок записи,
            content - текст записи ,   
        """  
        self.note_id += 1  
        note = Note(self.note_id , title, content)  
        self.notes.append(note)  
  
    def save_notes(self): 
        """  
        Сохраняет запись в блокноте 
   
        """   
        notes_data = []  
        for note in self.notes:  
            note_data = {  
                'id': note.id,  
                'title': note.title,  
                'content': note.content,  
                'created_at': note.created_at.strftime('%Y-%m-%d %H:%M:%S'),  
                'updated_at': note.updated_at.strftime('%Y-%m-%d %H:%M:%S')  
            }  
            notes_data.append(note_data)  
  
        with open(self.name, 'w') as file:  
            json.dump(notes_data, file, indent=4)  
  
    def load_notes(self):
        """  
        Читает записи в блокноте 
   
        """  
        try:  
            with open(self.name, 'r') as file:  
                notes_data = json.load(file)  
                for note_data in notes_data:  
                    id = note_data['id']  
                    title = note_data['title']  
                    content = note_data['content']  
                    created_at = datetime.datetime.strptime(note_data['created_at'], '%Y-%m-%d %H:%M:%S')  
                    updated_at = datetime.datetime.strptime(note_data['updated_at'], '%Y-%m-%d %H:%M:%S')  
                    note = Note(id, title, content)  
                    note.created_at = created_at  
                    note.updated_at = updated_at  
                    self.notes.append(note)  
        except FileNotFoundError as e:  
            self.notes = [] 
    def list_notes_id(self,id):
        """  
        Выводит записи из блокнота по id

        Arg:
            id - id записи 
   
        """
        swithc = True
        if(id != ""):
            for note in self.notes:
                if (note.id == id): 
                    print(f"ID: {note.id}, Заголовок: {note.title}\nТекст: {note.content}\nДата/время создания: {note.created_at}\nДата/время последнего изменения: {note.updated_at}")
                    swithc = False
            if(swithc):
               print("\n!!!!!!!!!!!!Нет такого айди!!!!!!!!!!!\n") 
        else:
            print("Вы не указали айди")   
    def list_notes(self):
        """  
        Выводит записи из блокнота 

        """
        shitch = True
        for note in self.notes:  
            print(f"ID: {note.id}, Заголовок: {note.title}, Дата/время создания: {note.created_at}, Дата/время последнего изменения: {note.updated_at}")
            shitch = False
        if(shitch):
            print('\n!!!!!!!!!!!Список пуст!!!!!!!!!!!!\n')
    def list_notes_data(self, date):
        """  
        Выводит записи из блокнота по указонному дню

        Arg:
            date - date записи 
   
        """
        shitch = True 
        for note in self.notes:
            if (str(note.created_at).split(' ')[0] == date):  
                print(f"ID: {note.id}, Заголовок: {note.title}, Дата/время создания: {note.created_at}, Дата/время последнего изменения: {note.updated_at}")
                shitch= False
        if(shitch):
            print('\n!!!!!!!!!!!Список пуст!!!!!!!!!!!!\n')
    def edit_note(self, note_id, new_title, new_content):
        """  
        Обнавляет записи из блокнота по id

        Arg:
            note_id - id записи, 
            new_title - заголовок записи, 
            new_content - текст записи, 
   
        """  
        for note in self.notes:  
            if note.id == note_id:  
                note.update(new_title, new_content)  
                return True  
        return False  
  
    def delete_note(self, note_id): 
        """  
        Удалят записи из блокнота по id

        Arg:
            id - id записи 
   
        """ 
        for note in self.notes:  
            if note.id == note_id:  
                self.notes.remove(note)  
                return True  
        return False  
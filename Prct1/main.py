from NotesManager import *
 

if __name__ == "__main__": 

    while True:
        name = input("Укажите имя файла: ")
        if((name!= None) and (name != '')):
            break
        else:
            print("Неправильно указаное имя!")

    notes_manager = NotesManager(name=name)  
  
    while True:  
        print("1. Создать заметку")
        if(os.path.exists(f"{name}.json")):
            print("2. Просмотреть заметоку по id")
            print("3. Просмотреть список заметок") 
            print("4. Просмотреть список заметок по дате")  
            print("5. Редактировать заметку")  
            print("6. Удалить заметку")  
        print("0. Выход")  
  
        choice = input("Выберите действие: ")  
  
        if choice == "1":  
            title = input("Введите заголовок заметки: ")  
            content = input("Введите содержимое заметки: ")  
            notes_manager.create_note(title, content)  
            notes_manager.save_notes()  
            print("Заметка создана!")  
        elif choice == "2": 
            try:
                id = int(input("Укажите id: ")) 
            except ValueError:
                print('\n!!!!!!!!!!!Указывайте только цифры!!!!!!!!!!!\n')
                continue 
            notes_manager.list_notes_id(id)
        elif choice == "3":  
            notes_manager.list_notes()
        elif choice == "4":  
            data_choise = input("Укажите дату в формате гггг-мм-дд: ")
            notes_manager.list_notes_data(data_choise)   
        elif choice == "5": 
            try:
                note_id = int(input("Введите ID заметки для редактирования: "))
            except ValueError:
                print('\n!!!!!!!!!!!Указывайте только цифры!!!!!!!!!!!\n')
                continue   
            new_title = input("Введите новый заголовок заметки: ")  
            new_content = input("Введите новое содержимое заметки: ")  
            if notes_manager.edit_note(note_id, new_title, new_content):  
                notes_manager.save_notes()  
                print("Заметка отредактирована!")  
            else:  
                print("Заметка с указанным ID не найдена.")  
        elif choice == "6":  
            try:
                note_id = int(input("Введите ID заметки для удаления: "))
            except ValueError:
                print('\n!!!!!!!!!!!Указывайте только цифры!!!!!!!!!!!\n')
                continue
            if notes_manager.delete_note(note_id):  
                notes_manager.save_notes()  
                print("Заметка удалена!")  
            else:  
                print("\n!!!!!!!!!!!Заметка с указанным ID не найдена.!!!!!!!!!!!\n")  
        elif choice == "0":  
            break  
        else:  
            print("\n!!!!!!!!!!!Неверный выбор. Пожалуйста, попробуйте снова.!!!!!!!!!!!\n")  
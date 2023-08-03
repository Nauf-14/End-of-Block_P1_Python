# Необходимо написать проект, содержащий функционал работы с заметками. 
# Программа должна уметь создавать заметку, сохранять её, читать список заметок, 
# редактировать заметку, удалять заметку.

import json
from datetime import datetime

def read_notes():
    try:
        with open("notes.json", "r") as file:
            notes_data = json.load(file)
            return notes_data
    except FileNotFoundError:
        return []

def save_notes(notes_data):
    with open("notes.json", "w") as file:
        json.dump(notes_data, file)

def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    note_id = datetime.now().strftime("%Y%m%d%H%M%S")  # Создаем идентификатор заметки на основе времени
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "created_at": created_at,
        "updated_at": created_at
    }
    return note

def list_notes(notes_data):
    for note in notes_data:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['body']}")
        print(f"Дата создания: {note['created_at']}")
        print(f"Дата обновления: {note['updated_at']}")
        print("-" * 30)

def find_note_by_id(notes_data, note_id):
    for note in notes_data:
        if note["id"] == note_id:
            return note
    return None

def update_note(note):
    title = input("Введите новый заголовок заметки: ")
    body = input("Введите новый текст заметки: ")
    note["title"] = title
    note["body"] = body
    note["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def delete_note(notes_data, note_id):
    for note in notes_data:
        if note["id"] == note_id:
            notes_data.remove(note)
            return True
    return False

def main():
    notes_data = read_notes()

    while True:
        print("\nМеню:")
        print("1. Показать все заметки")
        print("2. Показать заметку по ID")
        print("3. Создать новую заметку")
        print("4. Обновить заметку")
        print("5. Удалить заметку")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            list_notes(notes_data)
        elif choice == "2":
            note_id = input("Введите ID заметки: ")
            note = find_note_by_id(notes_data, note_id)
            if note:
                print("ID:", note['id'])
                print("Заголовок:", note['title'])
                print("Текст:", note['body'])
                print("Дата создания:", note['created_at'])
                print("Дата обновления:", note['updated_at'])
            else:
                print("Заметка с таким ID не найдена.")
        elif choice == "3":
            note = create_note()
            notes_data.append(note)
            save_notes(notes_data)
            print("Заметка успешно создана.")
        elif choice == "4":
            note_id = input("Введите ID заметки для обновления: ")
            note = find_note_by_id(notes_data, note_id)
            if note:
                update_note(note)
                save_notes(notes_data)
                print("Заметка успешно обновлена.")
            else:
                print("Заметка с таким ID не найдена.")
        elif choice == "5":
            note_id = input("Введите ID заметки для удаления: ")
            if delete_note(notes_data, note_id):
                save_notes(notes_data)
                print("Заметка успешно удалена.")
            else:
                print("Заметка с таким ID не найдена.")
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()

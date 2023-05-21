# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.

from os import path

file_base = "base.txt"
all_data = []
last_id = 1

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_records():
    global all_data, last_id

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
        return []

def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty base!\n")

def add_data(last_id):
    global all_data
    
    print('Enter "LAST NAME" "FIRST NAME" "MIDDLE NAME" "PHONE NUMBER"')
    print('To exit, enter "EXIT":')
    temp_data = []
    work = True
    while work:
        enter = input()
        if enter.upper() == 'EXIT':
            work = False
        elif len(enter.split()) != 4:
            print('Entered incorrectly. Check the entered data')
        else:
            temp_data.append(str(last_id) + ' ' + enter)
            last_id += 1
    
    if temp_data:
        with open(file_base, 'a', encoding="utf-8") as f:
            f.write(*temp_data)

def search():
    pass

def change_data():
    pass

def delete():
    pass

def main_export_import():
    pass

def main_menu():
    work = True
    while work:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all\n"
                       "2. Add data\n"
                       "3. Search\n"
                       "4. Change data\n"
                       "5. Delete\n"
                       "6. Export/Import\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                work = False
            case _:
                print("Try again!\n")

main_menu()
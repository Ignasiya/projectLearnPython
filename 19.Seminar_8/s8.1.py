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
        print(*all_data, sep="\n", end="\n")
    else:
        print("Empty base!\n")
    print()

def add_data(last_id):
    print('Enter "LAST NAME" "FIRST NAME" "MIDDLE NAME" "PHONE NUMBER"')
    print('To exit, enter "EXIT":')
    temp_data = []
    work = True
    last_id += 1
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
            print(*temp_data, sep='\n', end='\n', file=f)

def search():
    enter = input('Enter the search element: ').upper()
    if enter == '':
        print("Empty search element!\n")
    elif all_data:
        print(*list(filter(lambda x: x.upper().find(enter) >= 0, all_data)), sep='\n', end='\n')
    else:
        print("Empty base or search element!\n")
    print()

def change_data():
    global all_data

    enter = input('Enter the line ID: ')
    if enter.isdigit():
        if all_data:            
            work = False
            for i in range(len(all_data)):
                if enter == all_data[i][0]:
                    enter = str(i)
                    work = True
                    break
            else:
                print("There is no such line\n")
            while work:
                change_string = all_data[int(enter)]
                print("Change string:", change_string)
                answer = input('Do you want to make changes?:\n'
                                '1. Yes\n'
                                '2. No\n')
                match answer:
                    case "1":
                        new_enter = input('Enter new "LAST NAME" "FIRST NAME" "MIDDLE NAME" "PHONE NUMBER":\n')
                        if len(new_enter.split()) != 4:
                            print('Entered incorrectly. Check the entered data\n')
                        else:
                            all_data[int(enter)] = (all_data[int(enter)][0] + ' ' + new_enter)
                            work = False
                    case "2":
                        work = False
                    case _:
                        print("Try again!\n")
            
            with open(file_base, 'w', encoding="utf-8") as f:
                print(*all_data, sep='\n', end='\n', file=f)
        else:
            print("Empty base!\n")
    else:
        print("Incorrect ID\n")

def delete():
    global all_data

    enter = input('Enter the ID of the row to delete: ')
    if enter.isdigit():
        if all_data:            
            work = False
            for i in range(len(all_data)):
                if enter == all_data[i][0]:
                    enter = str(i)
                    work = True
                    break
            else:
                print("There is no such line\n")
            while work:
                delete_string = all_data[int(enter)]
                print("Change string:", delete_string)
                answer = input('Do you want to delete this line?:\n'
                                '1. Yes\n'
                                '2. No\n')
                match answer:
                    case "1":
                        del all_data[int(enter)]
                        work = False
                    case "2":
                        work = False
                    case _:
                        print("Try again!\n")
                
            with open(file_base, 'w', encoding="utf-8") as f:
                print(*all_data, sep='\n', end='\n', file=f)
        else:
            print("Empty base!\n")
    else:
        print("Incorrect ID\n")    

def main_export_import(last_id):
    work = True
    while work:
        answer = input('1. Export\n'
                        '2. Import\n')
        match answer:
            case "1":
                start_id = input('Enter the initial ID for export: ')
                for i in range(len(all_data)):
                    if start_id == all_data[i][0]:
                        start_id = i
                        break
                else:
                    print("There is no such ID\n")
                    return
                
                end_id = input('Enter the destination ID for export: ')
                for i in range(len(all_data)):
                    if end_id == all_data[i][0]:
                        end_id = i
                        break
                else:
                    print("There is no such ID\n")
                    return
                new_name_file = input('Enter the name of the new file: ')
                with open(new_name_file + '.txt', 'w', encoding="utf-8") as f:
                    for i in range(start_id, end_id + 1):
                        print(all_data[i], sep='\n', end='\n', file=f)
                work = False
            case "2":
                name_file = input('Enter the name of the file to import: ').strip()
                if not path.exists(name_file + '.txt'):
                    print("There is no such file\n")                    
                else:
                    with open(name_file + '.txt', 'r', encoding="utf-8") as new_f:
                        temp_data = []
                        last_id += 1
                        for i in new_f:
                            if len(i.split()) != 4:
                                print('The string must contain 4 elements (without ID)\n')
                                return
                            else:
                                temp_data.append(str(last_id) + ' ' +i.strip())
                                last_id += 1
                    if temp_data:
                        with open(file_base, 'a', encoding="utf-8") as f:
                            print(*temp_data, sep='\n', end='\n', file=f)
                    else:
                        print("Empty base!\n")                        
                work = False
            case _:
                print("Try again!\n")

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
                add_data(last_id)
            case "3":
                search()
            case "4":
                change_data()
            case "5":
                delete()
            case "6":
                main_export_import(last_id)
            case "7":
                work = False
            case _:
                print("Try again!\n")

main_menu()
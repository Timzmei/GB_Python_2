import os
import csv

def create_note(text):
    line = text
    with open('file.txt', 'a') as file:
        file.write(f'{line}\n')
        
        
def load_contacts():
    with open('file.txt', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        contacts = list(reader)
    return contacts


def print_contacts():
    with open('file.txt', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        # print(file.readlines())
        for contact in list(reader):
            print(f'{contact[0]} {contact[1]} {contact[2]}: {contact[3]}')
            
def print_contacts(contacts):
    for contact in contacts:
        print(f'{contact[0]} {contact[1]} {contact[2]}: {contact[3]}')


def save_contacts(contacts):
    with open('file.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(contacts)

def search_contacts(contacts, name):
    results = []
    for contact in contacts:
        if name in contact[0] or name in contact[1] or name in contact[2] or name in contact[3]:
            results.append(contact)
    if len(results) == 0:
        print('Контакт не найден')
    else:
        print_contacts(results)
        return results

# def print_contacts(contacts):
#     for contact in contacts:
#         print(f'{contact[0]} {contact[1]} {contact[2]}: {contact[3]}')

def add_contact(contacts, last_name, first_name, middle_name, phone_number):
    contacts.append([last_name, first_name, middle_name, phone_number])
    save_contacts(contacts)



def delete_contact(contacts, name):
    results = search_contacts(contacts, name)
    if len(results) > 1:
        print('Найдено несколько контактов')
        index = int(input('Выберите номер контакта для удаления: '))
        contact = results[index]
    else:
        contact = results[0]
    print(f'Выбран контакт для удаления: {contact[0]} {contact[1]} {contact[2]}: {contact[3]}')
    contacts.remove(contact)
    save_contacts(contacts)
    print('Контакт удален')
    
def edit_contact(contacts, name):
    results = search_contacts(contacts, name)
    if len(results) > 1:
        print('Найдено несколько контактов')
        index = int(input('Выберите номер контакта для редактирования: '))
        contact = results[index]
    else:
        contact = results[0]
    print(f'Редактируем контакт: {contact[0]} {contact[1]} {contact[2]}: {contact[3]}')
    last_name = input('Введите фамилию (оставьте пустым, чтобы сохранить текущее значение): ')
    first_name = input('Введите имя (оставьте пустым, чтобы сохранить текущее значение): ')
    middle_name = input('Введите отчество (оставьте пустым, чтобы сохранить текущее значение): ')
    phone_number = input('Введите телефон (оставьте пустым, чтобы сохранить текущее значение): ')
    if last_name == '':
        last_name = contact[0]
    if first_name == '':
        first_name = contact[1]
    if middle_name == '':
        middle_name = contact[2]
    if phone_number == '':
        phone_number = contact[3]
    print(f'Обновленный контакт: {last_name} {first_name} {middle_name}: {phone_number}')
    print(contact)
    contacts.remove(contact)
    add_contact(contacts, last_name, first_name, middle_name, phone_number)


def read_file(filename):
    with open('file.txt') as file:
        # print(list(file.readlines()))
        for contact in list(file.readlines()):
            print(f'{contact[0]} {contact[1]} {contact[2]}: {contact[3]}')


def main():
    # create_note('Guliev Timur Abrekovich +79174124652')
    # print(read_file('file.txt'))
    contacts = load_contacts()

    
    while True:
        print('1. Показать контакты')
        print('2. Найти контакты')
        print('3. Добавить контакт')
        print('4. Редактировать контакт')
        print('5. Удалить контакт')
        print('6. Выйти')
        number = input('Выберите действие: ')

        if number == '1':
            print_contacts(contacts)
        elif number == '2':
            name = input('Введите имя или телефон для поиска контакта: ')
            results = search_contacts(contacts, name)

        elif number == '3':
            last_name = input('Введите фамилию: ')
            first_name = input('Введите имя: ')
            middle_name = input('Введите отчество: ')
            phone = input('Введите телефон: ')
            add_contact(contacts, last_name, first_name, middle_name, phone)
            print('Контакт добавлен')
        elif number == '4':
            name = input('Выберите контакт для редактирования (введите имя или телефон): ')
            edit_contact(contacts, name)
        elif number == '5':
            name = input('Введите имя или телефон для удаления контакта: ')
            delete_contact(contacts, name)
        elif number == '6':
            break
        else:
            print('Выбор не распознан')
    
    
if __name__ == '__main__':
    main()
    
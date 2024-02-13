import csv
import string
import random 

def create_login(fio):
    '''
    Функция создания логина пользователя по строке ФИО

    fio – строка с именем, отчеством и фамилией пользователя
    '''
    name, patronymic, surname = fio.split()
    return f'{name[0]}{patronymic[0]}{surname}'

def create_password():
    '''
    Функция генерации пароля по требованиям
    '''
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    comma = '!?().'
    letters = lower + upper + digit + comma

    while True:
        password = ''.join(random.choices(letters, k=10))
        any_lower = any(char in password for char in lower)
        any_upper = any(char in password for char in upper)
        any_digit = any(char in password for char in digit)
        any_comma = any(char in password for char in comma)
        if any_lower + any_upper + any_digit + any_comma > 1: 
            return password

with open('grants.csv', 'r', encoding='cp1251') as file:
    researchers_list = list(csv.DictReader(file, delimiter=';'))

    for researcher in researchers_list:
        researcher['Login'] = create_login(researcher['Full_Name'])
        researcher['Password'] = create_password()

with open('grants_auths.csv', 'w', encoding='cp1251') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['id', 'Full_Name', 'Project_id', 'Nomination', 'Prize', 'Login', 'Password'])
    writer.writeheader()
    writer.writerows(researchers_list)


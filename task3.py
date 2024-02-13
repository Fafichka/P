import csv
# Linear search
with open('grants.csv', 'r', encoding='cp1251') as file:
    researchers_list = list(csv.DictReader(file, delimiter=';'))

    project_id = input()
    while project_id.lower() != 'стоп' and project_id != '':
        project_id = int(project_id)
        for researcher in researchers_list:
            if project_id == int(researcher['Project_id']):
                name, patronymic, surname = researcher['Full_Name'].split()
                prize = researcher["Prize"][:-3] if researcher['Prize'] != 'NULL' else 'NULL'
                print(f'Заявка № {project_id} Автор: {surname} {name[0]}.{patronymic[0]}. Сумма – {prize} тыс. руб.')
                break # если точно известно, что заявка уникальна (в файле, к сожалению, это не так)
        else:
            print('Такой заявки нет в реестре')
        project_id = input()

# Binary search
# with open('grants.csv', 'r', encoding='cp1251') as file:
#     researchers_list = list(csv.DictReader(file, delimiter=';'))
#     researchers_list = sorted(researchers_list, key=lambda x: int(x['Project_id']))


#     project_id = input()
#     while project_id.lower() != 'стоп' and project_id != '':
#         project_id = int(project_id)
        
#         left, right = 0, len(researchers_list) - 1
#         while left <= right:
#             middle = (left + right) // 2
#             if project_id == int(researchers_list[middle]['Project_id']):
#                 name, patronymic, surname = researchers_list[middle]['Full_Name'].split()
#                 print(f'Заявка № {project_id} Автор: {surname} {name[0]}.{patronymic[0]}. Сумма – {researchers_list[middle]["Prize"][:-3]} тыс. руб.')
#                 break # если известно, что заявка точно уникальна
#             elif project_id < int(researchers_list[middle]['Project_id']):
#                 right = middle - 1
#             else:
#                 left = middle + 1
#         else:
#             print('Такой заявки нет в реестре')
#         project_id = input()
import csv

with open('grants.csv', 'r', encoding='cp1251') as file:
    researchers_list = list(csv.DictReader(file, delimiter=';'))
    # находим данные по Агафье
    for researcher in researchers_list:
        if 'Агафья' in researcher['Full_Name'] and 'Ершова' in researcher['Full_Name']:
            print(f'Вы получили {researcher["Prize"]} рублей в конкурсе {researcher["Nomination"]} с номером заявки {researcher["Project_id"]}.')
            break
    # считаем сумму призов и их количество по каждой номинации среди известных значений
    sums, counts = {}, {}
    for researcher in researchers_list:
        if researcher["Prize"] != 'NULL':
            sums[researcher['Nomination']] = sums.get(researcher['Nomination'], 0) + int(researcher['Prize'])
            counts[researcher['Nomination']] = counts.get(researcher['Nomination'], 0) + 1
    # заменяем неизвестные значения на средние в номинации
    for researcher in researchers_list:
        if researcher['Prize'] == 'NULL':
            researcher['Prize'] = round(sums[researcher['Nomination']] // counts[researcher['Nomination']], -3)

# записываем обновлённые значения в файл grants_new.csv
with open('grants_new.csv', 'w', encoding='cp1251') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['id', 'Full_Name', 'Project_id', 'Nomination', 'Prize'])
    writer.writeheader()
    writer.writerows(researchers_list)

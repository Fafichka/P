import csv

def merge_sort(data):
    '''
    Функция сортировки методом слияния, осуществляющая разделение списка

    data – сортируемый список/массив
    '''
    if len(data) <= 1: return data
    mid = len(data) // 2
    left, right = merge_sort(data[:mid]), merge_sort(data[mid:])
    return merge(left, right, data)


def merge(left, right, merged):

    '''
    Вспомогательная функция для merge_sort, осуществляющая непосредственно слияние

    left, right – отсортированные списки/массивы, которые необходимо соединить
    merged – отсортированный результат слияния left и merged
    '''
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        left_value = int(left[left_cursor]['Prize']) if left[left_cursor]['Prize'] != 'NULL' else 0
        right_value = int(right[right_cursor]['Prize']) if right[right_cursor]['Prize'] != 'NULL' else 0
        if left_value >= right_value:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


with open('grants.csv', 'r', encoding='cp1251') as file:
    researchers_list = list(csv.DictReader(file, delimiter=';'))

    merge_sort(researchers_list)

    top_position = 0
    print(f'Номинация: Проект будущего')
    for researcher in researchers_list:
        if researcher['Nomination'] == 'Проект будущего':
            top_position += 1
            name, patronymic, surname = researcher['Full_Name'].split()
            print(f'Топ-{top_position}: {surname} {name[0]}.')
            if top_position == 3: break

# with open('grants_sort.csv', 'w', encoding='cp1251') as file:
#     writer = csv.DictWriter(file, delimiter=';', fieldnames=['id', 'Full_Name', 'Project_id', 'Nomination', 'Prize'])
#     writer.writeheader()
#     writer.writerows(researchers_list)

import csv

def create_hash(s):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet += alphabet.upper()
    alphabet += ' '
    p, m = 67, 10**9 + 9  # 1e9 + 9
    hash = 0
    dictionary = {alphabet[i]: i + 1  for i in range(len(alphabet))}
    for i in range(len(s)):
        hash += dictionary[s[i]] * (i + 1)**2
    hash *= (p**(len(s)) - 1)
    hash += p
    return hash % m

with open('grants.csv', 'r', encoding='cp1251') as file:
    researchers_list = list(csv.DictReader(file, delimiter=';'))

    for researcher in researchers_list:
        researcher['id'] = create_hash(researcher['Full_Name'])

with open('grants_hash.csv', 'w', encoding='cp1251') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['id', 'Full_Name', 'Project_id', 'Nomination', 'Prize'])
    writer.writeheader()
    writer.writerows(researchers_list)
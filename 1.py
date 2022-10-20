# Написать программу по импорту и экспорту телефонного справочника состоящий из N тысяч строк,
# содержащих информацию о неких пользователях.
# Предлагаемые поля: id, имя, фамилия, день рождения, место работы, номер телефона (может быть
# несколько). В качестве символа разделителя использовать пустую строку (пустой символ).
# Программа должна быть модульной (как показывалось на уроке). Она должна уметь генерировать
# справочник и сохранять его в файл при необходимости (экспорт) или загружать (импорт). Также
# необходимо организовать просмотр информации из справочника (генерируемого или загружаемого).
# В качестве формата файла можно использовать форматы csv, json, xml

import random
import csv

def randUser(how):
    firstName = ['Иван','Андрей','Олег','Константин','Аркадий','Фёдр','Алексей','Евгений','Николай','Александр','Виктор','Максим','Пётр','Крилл']
    secondName = ['Иванов','Андреев','Романов','Капустин','Стрелков','Медведев','Звонов','Рунов','Меценгендлер','Марцинкевич','Шаломов']
    dayInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
    work = ['Евраз','Этажи','Сбербанк','ВТБ','Связной','Мегафон','Яндекс','Диливери']
    users = []
    for i in range(how):
        user = str(random.randint(10000,99999))+' '
        user = user + firstName[random.randint(0, len(firstName)-1)]+' '
        user = user + secondName[random.randint(0, len(secondName)-1)]+' '
        month = random.randint(1, 12)
        user = user + str(random.randint(1,dayInMonth[month-1]))+'.'+str(month)+'.'+str(random.randint(1960,2004))+' '
        user = user + work[random.randint(0, len(work)-1)]
        for j in range(random.randint(1,2)):
            user = user + ' +7-' + str(random.randint(900,950))+'-'
            user = user + str(random.randint(100,999))+'-'
            user = user + str(random.randint(10,99))+'-'
            user = user + str(random.randint(10,99))
        users.append(user)
        
    print('Список сгенерирован')
    return users

def saveUsers(users):
    if len(users) == 0:
        print('Списка нет')
    else:
        with open('users.csv', 'w') as f:
            writer = csv.writer(f, delimiter = ' ', lineterminator="\r")
            for i in range(len(users)):
                writer.writerow(users[i].split(' '))
        print('Список сохранён')
        f.close()
    
def loadUsers():
    lst = []
    with open('users.csv') as f:
        reader = csv.reader(f, delimiter = " ")
        for row in reader:
            user = ''
            for column in row:
                user = user + column + ' '
            lst.append(user)
    print('Список загружен')
    f.close()
    return lst

def showUsers(users):
    if len(users) == 0:
        print('Списка нет')
    else:
        for i in range(len(users)):
            print(users[i])

def interf(users):
    a = input('Сгенерировать список (r), загрузить список(l), сохранить список(s), показать список(sh): ')
    if a == 'r':
        how = int(input('Кол-во строк: '))
        users = randUser(how)
    elif a == 'l':
        users = loadUsers()
    elif a == 's':
        saveUsers(users)
    elif a == 'sh':
        showUsers(users)
    else:
        print('Введите корректный код')
    interf(users)


users = []
interf(users)
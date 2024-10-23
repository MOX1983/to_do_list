import time
import json
import re

def writJson(data):
    try:
        with open('tasks.json', 'w') as file:
            json.dump(data, file, indent=' ')
            print("записано :) ")
    except FileNotFoundError as ex:
        print(f"Ошибка: файл не найден - {ex}")

def readJson():
    try:
        with open('tasks.json') as file:
            rezolt = json.load(file)
            return rezolt
    except FileNotFoundError as ex:
        print(f"Ошибка: файл не найден - {ex}")

def newTask(data_dict, task, time_date):
    if re.fullmatch("\d\d/\d\d/\d{4} \d\d:\d\d", time_date):
        date = time.strptime(time_date, "%d/%m/%Y %H:%M")
        tme = time.strptime(time_date, "%d/%m/%Y %H:%M")
    else:
        date = time.localtime()
        tme = time.strptime(time_date, "%H:%M")

    if time.strftime("%d/%m/%Y", date) not in data_dict:
        data_dict[time.strftime("%d/%m/%Y", date)] = dict()
    data_dict[time.strftime("%d/%m/%Y", date)][time.strftime("%H:%M", tme)] = task

    print("задачa записанa :)")
    writJson(data_dict)

def printTask(data_dict):
    print("На сегодня: ")
    for key in data_dict[time.strftime("%d/%m/%Y", time.localtime())]:
        print(f"{key} --- {data_dict[time.strftime("%d/%m/%Y", time.localtime())][key]}")

def deleteTask(data_dict):
    time_date = input("введите время и дату задачи %m/%d/%Y %H:%M --- ")

    date = time.strptime(time_date, "%d/%m/%Y %H:%M")
    tme = time.strptime(time_date, "%d/%m/%Y %H:%M")

    print(f"теперь задачи --- {data_dict[time.strftime("%d/%m/%Y", date)].pop(time.strftime("%H:%M", tme))}, нет ")
    writJson(data_dict)

def main():
    data_dict = readJson()

    task = input("Введите задачу: ")
    date_time = input("дату и время задачи : ")
    newTask(data_dict, task, date_time)
    print(data_dict)

    print('')
    printTask(data_dict)

    print('')
    deleteTask(data_dict)


if __name__ == "__main__":
    main()
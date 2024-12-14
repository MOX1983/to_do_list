import json
import re
import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

def writJson(data, printjson):
    try:
        with open('tasks.json', 'w') as file:
            json.dump(data, file, indent=' ')
            printjson['text'] = ("записано :) ")
    except FileNotFoundError as ex:
        show_result(ex)

def readJson():
    try:
        with open('tasks.json') as file:
            rezolt = json.load(file)
            return rezolt
    except FileNotFoundError as ex:
        show_result(ex)

def newTask(data_dict, task, time_date, printjson):
    try:
        if re.fullmatch("\d\d/\d\d/\d{4} \d\d:\d\d", time_date):
            date = time.strptime(time_date, "%d/%m/%Y %H:%M")
            tme = time.strptime(time_date, "%d/%m/%Y %H:%M")
        else:
            date = time.localtime()
            tme = time.strptime(time_date, "%H:%M")

        if time.strftime("%d/%m/%Y", date) not in data_dict:
            data_dict[time.strftime("%d/%m/%Y", date)] = dict()
        data_dict[time.strftime("%d/%m/%Y", date)][time.strftime("%H:%M", tme)] = task

        b = True

    except Exception as ex:
        show_result(ex)
        b = False
    if b:
        printjson['text'] = "задачa записанa :)"
        writJson(data_dict, printjson)

def printTask(data_dict, printjson):
    printjson['text'] = ("На сегодня: ")
    for key in data_dict[time.strftime("%d/%m/%Y", time.localtime())]:
        printjson['text'] += (f"\n{key} --- {data_dict[time.strftime("%d/%m/%Y", time.localtime())][key]}\n")

def deleteTask(data_dict,time_date, printjson):

    date = time.strptime(time_date, "%d/%m/%Y %H:%M")
    tme = time.strptime(time_date, "%d/%m/%Y %H:%M")

    printjson['text'] = (f"теперь задачи --- {data_dict[time.strftime("%d/%m/%Y", date)].pop(time.strftime("%H:%M", tme))}, нет ")
    writJson(data_dict, printjson)

def show_result(ex):
    messagebox.showinfo('Результат', f'Ошибка {ex}')

data_dict = readJson()
window = Tk()
window.title("To Do ;]")
window.geometry('500x250')

method_lbl = Label(window, text="Выберите ")
method_lbl.grid(row=0, column=0)

lbl = Label(window, text="Введите задачу:")
lbl.grid(column=0, row=1)
txt = Entry(window)
txt.grid(column=1, row=1)
lbltime = Label(window, text="дату и время задачи (%d/%m/%Y %H:%M): ")
lbltime.grid(column=0, row=2)
txttime = Entry(window)
txttime.grid(column=1, row=2)

btn = Button(window, text="добавить задачу ", command=lambda: newTask(data_dict, txt.get(), txttime.get(), printjson))
btn.grid(column=0, row=4)

printjson = Label(window, text="")
printjson.grid(column=0, row=5)

prbtn = Button(window, text="print", command=lambda: printTask(data_dict, printjson))
prbtn.grid(column=0, row=6)

lbltime = Label(window, text="дату и время задачи (%d/%m/%Y %H:%M): ")
lbltime.grid(column=0, row=7)
txttime = Entry(window)
txttime.grid(column=1, row=7)

btn = Button(window, text="Удалить задачу", command=lambda: deleteTask(data_dict, txttime.get(), printjson))
btn.grid(column=0, row=8)

printjson = Label(window, text="")
printjson.grid(column=0, row=9)

prbtn = Button(window, text="print", command=lambda: printTask(data_dict, printjson))
prbtn.grid(column=0, row=10)

window.mainloop()
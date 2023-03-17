import sys
from tkinter import *
import random
from tkinter import messagebox


def motion_mouse(*args, **kwargs):
    """Наведение на кнопку Yes

    :param args:
    :param kwargs:
    :return:
    """
    btn_yes.place(x=random.randint(0, 500), y=random.randint(0, 300))


def no_button_click(*args, **kwargs):
    """Нажатие на кнопку No

    :param args:
    :param kwargs:
    :return:
    """
    messagebox.showinfo('Вопрос', 'Спасибо, ваш голос учтен')
    sys.exit()


"""Создание параметров окна"""
root = Tk()  # Инициализация ткинтера
root.geometry('600x400')  # Параметры окна
root.resizable(width=False, height=False)  # Запрет на масштабирование
root['bg'] = 'white'  # Белый фон

"""Создание надписи"""
label = Label(root, text='Вы хотите увеличить зарплату?', font='Arial 20 bold', bg='white')  # Создание надписи
label.pack()

"""Создание кнопки да"""
btn_yes = Button(root, text='Да', font='Arial 20 bold')  # Создание кнопки да
btn_yes.place(x=80, y=100)  # Размещение кнопки
btn_yes.bind('<Enter>', motion_mouse)  # Enter: указатель мыши вошел в пределы виджета.

"""Создание кнопки нет"""
btn_no = Button(root, text='Нет', font='Arial 20 bold')  # Создание кнопки да
btn_no.place(x=450, y=100)  # Размещение кнопки
btn_no.bind('<ButtonPress>', no_button_click)

if __name__ == '__main__':
    root.mainloop()

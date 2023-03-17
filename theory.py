# name = 'Artem'  # Получение имени
# age = 21  # Получение возраста
#
# print('Меня зовут', name, 'Мне', age, 'год')
#
# print(f'Меня зовут {name}. Мне {age} год.')
#
#
# """Условия"""
# a = 22
# if a < 0:
#     print(f'Число {a} отрицательное')
# else:
#     print(f'Число {a} положительное')
#
# """Работа со строками"""
# b = 'ХоРоШо'
# print(b.lower())  # Приведение строки к нижнему регистру

"""Коллекции"""
names = ['Artem', 'Vasya', 'Petya', 'John']
# # print(names[1])
# print(names)
#
# names[1] = 'Ivan'
# print(names, end='\n\n')
#
# names.append('Vlad')
# print(names, end='\n\n')
#
# names.insert(1, 'Boris')
# print(names, end='\n\n')
#
# del names[2]
# print(names, end='\n\n')
#
# deleted = names.pop(2)
# print(names, end='\n\n')
# print(deleted, end='\n\n')
#
# names.remove('Vlad')
# print(names, end='\n\n')


"""Циклы"""
# for name in names:  # name = Artem -> name = Vasya -> name = Petya
#     if name == 'Artem':
#         continue
#         # break
#     print(name)

# grade = 2
#
# while grade > 0:
#     print(f'Снова {grade}??? Наказан!')
#     if grade == 10:
#         break
#     grade += 1  # То же самое grade = grade + 1


"""Функции"""


def light_edit(action='Включили'):
    for i in range(1, 6):
        print(f'{action} {i} лампу')


# light_edit(action='Включили')
# light_edit('Выключили')

# light_edit()


"""ООП - классы"""


# class Dog:
#     """Модель собаки"""
#
#     def __init__(self, name, age):
#         """Инициализация атрибутов name, age"""
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'Имя: {self.name}, Возраст: {self.age}'
#
#
# # some_dog = Dog(name='Шарик', age=10)
# # print(some_dog.age)
# # print(some_dog.name)
# # # some_dog = Dog(age=10, name='Шарик')
# # # some_dog = Dog('Шарик', 10)
# #
# # some_dog_2 = Dog('Бобик', 8)
# # print(some_dog_2)
#
# class Car:
#     """Проста модель автомобиля"""
#
#     def __init__(self, brand, model, year, color):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.color = color
#
#     def get_description(self):
#         """Описание автомобиля"""
#         description = f'{self.brand} | {self.model} | {self.color} | {self.year}'
#         return description
#
#
# car = Car(brand='BMW', model='X5', year=2017, color='white')
# print(car)

"""tkinter Canvas"""
from tkinter import *

root = Tk()
root.title('Canvas')
root.geometry('400x400')

canvas = Canvas(bg='white', width=250, height=250)
canvas.pack(anchor=CENTER, expand=True)

"""Создание линий"""
# canvas.create_line(10, 10, 10, 100, fill='black', activefill='red', width=10, dash=1)
# canvas.create_line(10, 30, 200, 30, fill='black', activefill='red', width=10, dash=1)
"""Создание прямоугольников"""
canvas.create_rectangle(10, 20, 200, 60, fill='', outline='black')


root.mainloop()

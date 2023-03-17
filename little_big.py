# little_big

number = 100
count = 1

while True:
    try:
        answer = int(input('Введите число: '))

        if answer == number:
            print('Вы угадали!')
            print(f'Кол-во попыток: {count}')
            break
        elif answer < number:
            print('Ваше число меньше загаданного')
            count += 1
        else:  # elif answer > number:
            print('Ваше число больше загаданного')
            count += 1

    # except ValueError:
    #     print(f'[ERROR] Данные должны иметь числовой тип')

    except Exception as ex:
        print(repr(ex))

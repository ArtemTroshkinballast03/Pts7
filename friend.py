print('Привет!')
name = input('Введите свое имя: ')
print(f'Приятно познакомиться, {name}')

answer = input('Как у тебя дела? ')

if answer.lower() == 'хорошо':
    print('Отлично, рад за тебя!')

elif answer.lower() == 'плохо':
    print('Мне жаль :(')

elif answer.lower() == 'нормально':
    print('Давай улучшим!')

else:
    print('Я тебя не понимаю')

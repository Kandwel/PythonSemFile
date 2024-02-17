from logger import input_data, print_data, copy_data


def interface():
    print('Здравствуйте! Это бот-помощник. \n'
          'Что вы хотите сделать \n'
          '1 - Записать данные \n'
          '2 - Вывести данные \n'
          '3 - Скопировать данные из одного файла в другой \n')
    command = int(input('Ваш выбор: '))

    while command < 1 or command > 3:
        command = int(input('Ошибка! Ваш выбор: '))

    if command == 1:
        input_data()
        main_fun()
    elif command == 2:
        print_data()
        main_fun()
    elif command == 3:
        copy_data()
        main_fun()

def main_fun():
    print('\nХотите продолжить? \n'
            '1 - Да \n'
            '2 - Нет \n')
    finish = int(input('Ваш выбор: '))

    while finish < 1 or finish > 2:
        finish = int(input('Ошибка! Ваш выбор: '))

    if finish == 1:
        interface()
    elif finish == 2:
        exit()

interface()

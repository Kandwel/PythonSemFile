from data_create import input_user_data
#from main import main_fun

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные? \n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')


def print_data():
    print('\n1 файл:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))
        
    print('2 файл:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))


def copy_data():
    print('Выберете файл: \n'
          '1 - Файл с записью в столбец \n'
          '2 - Файл с записью в строку')
    FileNumName = int(input('Ваш выбор: '))
    
    while FileNumName < 1 or FileNumName > 2:
        FileNumName = int(input('Ошибка! Ваш выбор: '))

    FileNumStrok = int(input('Введите номер строки данных для копирования: '))

    if (FileNumName == 1):
        FileName1 = 'data_first_variant.csv'
        FileName2 = 'data_second_variant.csv'
    elif (FileNumName == 2):
        FileName1 = 'data_second_variant.csv'
        FileName2 = 'data_first_variant.csv'

    with open(FileName1, 'r', encoding='utf-8') as file1:
        data1 = file1.readlines()
    
    with open(FileName2, 'a', encoding='utf-8') as file2:
        if 0 < FileNumStrok <= len(data1):
            CopiedData = data1[FileNumStrok - 1]
            file2.write(CopiedData)
            print(f'Данные из строки {FileNumStrok} файла {FileName1} успешно скопированы в файл {FileName2}.')
        else:
            print('Неверный номер строки данных.')
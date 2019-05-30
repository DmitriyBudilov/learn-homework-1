"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def input_string():
    '''
        Получение первичных строк.
    '''
    print('Для выхода введите Esc в одной из строк.')
    string_1 = input('Введите первую строку: ')
    string_2 = input('Введите вторую строку: ')
    return string_1, string_2

def output_result(string_1, string_2):
    '''
        Проверка корректности введенной информации.
        Если инф. корректна проверка по if.
    '''
    try:
        int(string_1) or int(string_2)
        return 0
    except ValueError:
        if string_1 == string_2:
            return 1
        elif string_1 != string_2 and len(string_1) > len(string_2):
            return 2
        elif string_1 != string_2 and string_2 == 'learn':
            return 3
        else:
            return 'Попробуй снова!'

def main():
    while True:
        string_1, string_2 = input_string()
        if string_1 == 'Esc' or string_2 == 'Ecs':
            break
        else:
            value = output_result(string_1, string_2)
            print(value)

if __name__ == '__main__':
    main()

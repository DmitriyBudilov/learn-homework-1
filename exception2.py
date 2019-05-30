"""

Домашнее задание №1

Исключения: приведение типов

* Напишите функцию get_summ(num_one, num_two), которая принимает 
  на вход два целых числа (int), складывает их и возвращает результат 
  сложения
* Оба аргумента нужно приводить к целому числу при помощи int() и 
  перехватывать исключение ValueError если приведение типов не сработало
    
"""

def users_string():
    while True:
        try:
            num_1 = int(input('Введите первое число: '))
            num_2 = int(input('Введите второе число: '))
            return num_1, num_2
        except ValueError:
            print('Вы ввели не число!')


def get_summ(num_1, num_2):
        result = num_1 + num_2
        return result

def main():
    num_1, num_2 = users_string()
    print(get_summ(num_1, num_2))

if __name__ == '__main__':
    main()


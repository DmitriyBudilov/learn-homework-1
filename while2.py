"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

dictionary_of_strings = {'Привет!': 'Привет!','Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую', 'На каком языке?': 'На python'}


def answer():
    while True:
        users_question = input('Введите вопрос: ')
        if users_question == 'Пока!':
            print('Пока!')
            break
        elif users_question in dictionary_of_strings:
            print(dictionary_of_strings[users_question])
        else:
            pass


def main():
    answer()

if __name__ == '__main__':
    main()

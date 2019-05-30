"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
dictionary_of_strings = {'Привет!': 'Привет!','Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую', 'На каком языке?': 'На python'}

def ask_user():
    while True:
        try:
            users_question = input('Введите вопрос: ')
            if users_question in dictionary_of_strings:
                print(dictionary_of_strings[users_question])
        except KeyboardInterrupt:
            print('\nПока!')
            break

if __name__ == '__main__':
    ask_user()

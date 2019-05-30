"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

school = [{'school_class': '4А', 'scores': [3, 4, 5, 4, 4, 5, 3]},
          {'school_class': '4Б', 'scores': [3, 4, 5, 4, 4, 3, 3]},
          {'school_class': '4В', 'scores': [5, 4, 5, 5, 4, 5, 3]}]

def average_score(scores):
    '''
        Вычисление среднего значения.
    '''
    average = sum(scores)/len(scores)
    return average

def scores(school_dictionary):
    for value in school_dictionary:
        print('Средняя оценка класса {school_class} - {score} балла.'.format(school_class=value['school_class'],
                                                                      score = round(average_score(value['scores']), 1)))
def school_average(school_dictionary):
    number_of_students = 0
    general_average = 0
    for value in school_dictionary:
        number_of_students += len(value['scores'])
        general_average += sum(value['scores'])
    return general_average/number_of_students

def main():
    scores(school)
    general_average = school_average(school)
    print('Средняя оценка по школе - {} балла.'.format(round(general_average, 1)))

if __name__ == '__main__':
    main()


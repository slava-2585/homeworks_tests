import requests


courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]


def popular_name(courses, mentors):
    all_list = []
    [all_list.extend(m) for m in mentors]
    all_names_list = [mentor.split()[0].strip() for mentor in all_list]
    unique_names = set(all_names_list)
    all_names_sorted = sorted(list(unique_names))
    popular = [[name, all_names_list.count(name)] for name in unique_names]

    popular.sort(key=lambda x: x[1], reverse=True)
    top_3 = popular[:3]
    res = [f'{names}: {count} раз(а)' for names, count in top_3]
    # print(', '.join(res))
    return res


def cook_book(person):
    cook_book = [
        ['салат',
         [
             ['картофель', 100, 'гр.'],
             ['морковь', 50, 'гр.'],
             ['огурцы', 50, 'гр.'],
             ['горошек', 30, 'гр.'],
             ['майонез', 70, 'мл.'],
         ]
         ],
        ['пицца',
         [
             ['сыр', 50, 'гр.'],
             ['томаты', 50, 'гр.'],
             ['тесто', 100, 'гр.'],
             ['бекон', 30, 'гр.'],
             ['колбаса', 30, 'гр.'],
             ['грибы', 20, 'гр.'],
         ],
         ],
        ['фруктовый десерт',
         [
             ['хурма', 60, 'гр.'],
             ['киви', 60, 'гр.'],
             ['творог', 60, 'гр.'],
             ['сахар', 10, 'гр.'],
             ['мед', 50, 'мл.'],
         ]
         ]
    ]

    for dish, ingredients in cook_book:
        res = f'{dish.capitalize()}:\n' + '\n'.join(f'{ing}, {q * person}{measure}' for ing, q, measure in ingredients)
    return res


def pair_girls_boys(girls, boys):
    if len(boys) == len(girls):
        boys.sort()
        girls.sort()
        pair = list(zip(boys, girls))
        res = '\n'.join(map(' and '.join, pair))
    else:
        res = 'Неверное количество человек'
    return res


def make_folder_yandex(name):
    with open('token.txt', 'r') as file_object:
        token = file_object.readline()
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    url = f'https://cloud-api.yandex.net/v1/disk/resources?path={name}'
    response = requests.put(url, headers=headers)
    return response.status_code


if __name__ == '__main__':
    # print(popular_name(courses, mentors))
    # print(cook_book(5))
    # print(pair_girls_boys(['Михаил', 'Александр', 'Владимир'], ['Нина', 'Вика', 'Ольга']))
    print(make_folder_yandex('new'))
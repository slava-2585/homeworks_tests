from unittest import TestCase, expectedFailure, main
import requests
from main import popular_name, cook_book, pair_girls_boys, make_folder_yandex


class TestPopularName(TestCase):
    def setUp(self):
        self.courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
                        "Frontend-разработчик с нуля"]

        self.mentors = [
            ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
             "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
             "Азамат Искаков",
             "Роман Гордиенко"],
            ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
             "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
             "Никита Шумский",
             "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов",
             "Евгений Грязнов",
             "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
             "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
             "Денис Ежков",
             "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
            ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
             "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин",
             "Михаил Ларченко"]
        ]

    def test_equal(self):
        res = popular_name(self.courses, self.mentors)
        expected = ['Александр: 10 раз(а)', 'Евгений: 5 раз(а)', 'Максим: 4 раз(а)']
        self.assertEqual(res, expected)

    def test_in_list(self):
        res = popular_name(self.courses, self.mentors)
        self.assertIn('Александр: 10 раз(а)', res)

    def test_list(self):
        res = popular_name(self.courses, self.mentors)
        self.assertIsInstance(res, list)

    def test_book(self):
        res = cook_book(5)
        expected = 'хурма, 300гр.'
        self.assertIn(expected, res)

    def test_pair_girls_boys(self):
        girls = ['Нина', 'Вика', 'Ольга']
        boys = ['Михаил', 'Александр', 'Владимир']
        res = pair_girls_boys(boys, girls)
        expected = 'Вика and Александр\nНина and Владимир\nОльга and Михаил'
        self.assertEqual(res, expected)

    def test_status_code(self):
        res = make_folder_yandex('new2')
        expected = 201
        self.assertEqual(res, expected)

    def test_make_folder_error(self):
        res = make_folder_yandex('vk')
        expected = 409
        self.assertEqual(res, expected)

    def test_make_folder_disk(self):
        make_folder_yandex('new')
        with open('token.txt', 'r') as file_object:
            token = file_object.readline()
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        url = f'https://cloud-api.yandex.net/v1/disk/resources?path=new'
        response = requests.get(url, headers=headers)
        res = response.status_code
        expected = 200
        self.assertEqual(res, expected)


if __name__ == '__main__':
    main()

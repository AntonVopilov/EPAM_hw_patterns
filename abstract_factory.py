"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.
С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.
"""

import yaml


class AbstractFood(object):
    def create_first(self, menu, day):
        raise NotImplementedError()

    def create_second(self, menu, day):
        raise NotImplementedError()

    def create_drink(self, menu, day):
        raise NotImplementedError()


class FoodVegan(AbstractFood):
    def __init__(self):
        self._meny_type = self.__class__.__name__.split('Food')[1].lower()

    def create_first(self, menu: dict, day: str):
        print('First courses for ', self._meny_type, ' is ', menu[day]['first_courses'][self._meny_type])

    def create_second(self, menu: dict, day: str):
        print('Second courses for ', self._meny_type, ' is ', menu[day]['second_courses'][self._meny_type])

    def create_drink(self, menu: dict, day: str):
        print('Drinks courses for ', self._meny_type, ' is ', menu[day]['drinks'][self._meny_type])


class FoodChild(AbstractFood):
    def __init__(self):
        self._meny_type = self.__class__.__name__.split('Food')[1].lower()

    def create_first(self, menu: dict, day: str):
        print('First courses for ', self._meny_type, ' is ', menu[day]['first_courses'][self._meny_type])

    def create_second(self, menu: dict, day: str):
        print('Second courses for ', self._meny_type, ' is ', menu[day]['second_courses'][self._meny_type])

    def create_drink(self, menu: dict, day: str):
        print('Drinks courses for ', self._meny_type, ' is ', menu[day]['drinks'][self._meny_type])


class FoodChina(AbstractFood):
    def __init__(self):
        self._meny_type = self.__class__.__name__.split('Food')[1].lower()

    def create_first(self, menu: dict, day: str):
        print('First courses for ', self._meny_type, ' is ', menu[day]['first_courses'][self._meny_type])

    def create_second(self, menu: dict, day: str):
        print('Second courses for ', self._meny_type, ' is ', menu[day]['second_courses'][self._meny_type])

    def create_drink(self, menu: dict, day: str):
        print('Drinks courses for ', self._meny_type, ' is ', menu[day]['drinks'][self._meny_type])


def client_code(FoodFactory: AbstractFood, menu: dict):
    FoodFactory.create_drink(menu, 'Monday')
    FoodFactory.create_first(menu, 'Wednesday')


with open('menu.yml') as f:
    menu = yaml.safe_load(f)

client_code(FoodChild(), menu)
client_code(FoodChina(), menu)
client_code(FoodVegan(), menu)

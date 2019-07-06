"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла
В итоге мы должны получить список недостающих ингридиентов.
"""


class Handler(object):

    def handle(self, holodos, recipe):
        raise NotImplementedError()


class HandlerEggs(Handler):

    def handle(self, holodos, recipe):
        food = self.__class__.__name__.split('Handler')[1].lower()
        if holodos[food] < recipe[food]:
            print(f"We need {recipe[food] - holodos[food]} {food}")
        else:
            print(f'Enough {food}')


class HandlerMilk(Handler):

    def handle(self, holodos, recipe):
        food = self.__class__.__name__.split('Handler')[1].lower()
        if holodos[food] < recipe[food]:
            print(f"We need {recipe[food] - holodos[food]} {food}")
        else:
            print(f'Enough {food}')


class HandlerButter(Handler):

    def handle(self, holodos, recipe):
        food = self.__class__.__name__.split('Handler')[1].lower()
        if holodos[food] < recipe[food]:
            print(f"We need {recipe[food] - holodos[food]} {food}")
        else:
            print(f'Enough {food}')


class HandlerOil(Handler):

    def handle(self, holodos, recipe):
        food = self.__class__.__name__.split('Handler')[1].lower()
        if holodos[food] < recipe[food]:
            print(f"We need {recipe[food] - holodos[food]} {food}")
        else:
            print(f'Enough {food}')


class HandlerFlour(Handler):

    def handle(self, holodos, recipe):
        food = self.__class__.__name__.split('Handler')[1].lower()
        if holodos[food] < recipe[food]:
            print(f"We need {recipe[food] - holodos[food]} {food}")
        else:
            print(f'Enough {food}')


class HandlerSugar(Handler):

    def handle(self, holodos, recipe):
        food = self.__class__.__name__.split('Handler')[1].lower()
        if holodos[food] < recipe[food]:
            print(f"We need {recipe[food] - holodos[food]} {food}")
        else:
            print(f'Enough {food}')


class MakeChain(object):
    def __init__(self):
        self._handlers = []

    def add_handler(self, h):
        self._handlers.append(h)
        return self

    def check_holodos(self, holodos, recipe):
        for h in self._handlers:
            h.handle(holodos, recipe)


chain = MakeChain()
chain.add_handler(HandlerEggs()).add_handler(HandlerButter()).add_handler(HandlerFlour()).add_handler(HandlerMilk())
chain.add_handler(HandlerSugar())

recipe = {
    'eggs': 2,
    'flour': 300,
    'milk': 0.5,
    'sugar': 100,
    'oil': 10,
    'butter': 120
}

holodos = {
    'eggs': 2,
    'flour': 300,
    'milk': 0.5,
    'sugar': 99,
    'oil': 10,
    'butter': 10
}
chain.check_holodos(holodos, recipe)

# 3. Дописать классы Human, House, SmallHouse.

class Human:
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = 'Нет'

    def info(self):
        print(f'Имя - {self.name}\nВозраст - {self.age}\nСумма на счету - {self.__money}\nДом - {self.__house}\n')

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def earn_money(self, money):
        self.__money += money
        print(f'Получено - {money}\nТекущий счет - {self.__money}\n')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.make_deal(house, price)
            print('Поздравляем с покупкой!\n')
        else:
            print('Недостаточно денег для покупки!\n')

    def make_deal(self, house, price):
        self.__money -= price
        self.__house = house


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price1 = self._price * (100 - discount) / 100
        print(f'Стоимость дома - {self._price}\nСкидка - {discount}\nОкончательная стоимость - {final_price1}\n')
        return final_price1


class SmallHouse(House):
    default_area = 'площадь 40м2'

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)

    def __str__(self):
        return SmallHouse.default_area


Alex = Human('Alex', 28)
Alex.info()
sm_house = SmallHouse(5000)
Alex.buy_house(sm_house, 7.5)
Alex.earn_money(7000)
Alex.info()
Alex.buy_house(sm_house, 7.5)
Alex.info()

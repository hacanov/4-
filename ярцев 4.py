class Human:
    default_name = "John Doe"
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.money = 0
        self.house = None

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Money: {self.money}, House: {self.house}")

    @staticmethod
    def default_info():
        print(f"Default name: {Human.default_name}, Default age: {Human.default_age}")

    def make_deal(self, house, price):
        if self.money >= price:
            self.money -= price
            self.house = house
            print("Deal successful!")
        else:
            print("Not enough money for the deal.")

    def earn_money(self, amount):
        self.money += amount

    def buy_house(self, house, discount=0):
        price = house._price * (1 - discount)
        self.make_deal(house, price)


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount)


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)


# Tests
Human.default_info()
person = Human("John", 25,)
person.info()
house = SmallHouse(20000)
person.buy_house(house)
person.earn_money(10000)
person.buy_house(house)
person.info()
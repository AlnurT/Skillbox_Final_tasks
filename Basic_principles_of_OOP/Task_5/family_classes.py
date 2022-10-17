class Home:
    """
    Базовый класс параметров Дома
    Attributes:
        __money: деньги
        __food: еда
        __cat_food: кошачий корм
        __dirt: грязь
        __total_salary: все заработанные деньги
        __total_eaten_food: вся съеденная еда и корм
        __number_of_fur_coat: общее количество купленных шуб
    """

    __money: int = 100
    __food: int = 50
    __cat_food: int = 30
    __dirt: int = 0

    __total_salary: int = 0
    __total_eaten_food: int = 0
    __number_of_fur_coat: int = 0

    def set_home_parameters(self, money: int, food: int, cat_food: int, dirt: int):
        self.__money = money
        self.__food = food
        self.__cat_food = cat_food
        self.__dirt = dirt

    def get_parameters(self):
        return (
            f"Дом:\n"
            f"Деньги: {self.__money}\n"
            f"Еда: {self.__food}\n"
            f"Кошачья еда: {self.__cat_food}\n"
            f"Грязь: {self.__dirt}\n"
        )

    def count_results_of_life(
        self, salary: int = 0, meal: int = 0, fur_coat: bool = False
    ):
        """
        Подсчитать итоги жизни: количество заработанных денег,
        количество съеденной еды и число купленных шуб
        :param salary: зарплата мужа
        :param meal: съеденная еда людьми и котом
        :param fur_coat: купленная шуба для жены
        """
        self.__total_salary += salary
        self.__total_eaten_food += meal
        self.__number_of_fur_coat += 1 if fur_coat else 0

    def get_total_salary(self) -> int:
        return self.__total_salary

    def get_total_eaten_food(self) -> int:
        return self.__total_eaten_food

    def get_number_of_fur_coat(self) -> int:
        return self.__number_of_fur_coat

    def set_money(
        self,
        fur_coat_cost: int = 0,
        salary: int = 0,
        food_cost: int = 0,
        cat_food_cost: int = 0,
    ):
        """
        Изменить количество денег в зависимости от событий: получение зарплаты,
        покупка шубы или покупка продуктов и кошачьего корма
        :param fur_coat_cost: стоимость шубы
        :param salary: зарплата
        :param food_cost: стоимость еды
        :param cat_food_cost: стоимость кошачьего корма
        """
        self.__money += salary - fur_coat_cost - (food_cost + cat_food_cost)

    def get_money(self) -> int:
        return self.__money

    def set_food(self, eaten_food: int = 0, purchased_food: int = 0):
        """
        Поесть или купить еду
        :param eaten_food: съеденная еда
        :param purchased_food: купленная еда
        """
        self.__food += purchased_food - eaten_food

    def get_food(self) -> int:
        return self.__food

    def set_cat_food(self, eaten_food: int = 0, purchased_food: int = 0):
        """
        Поесть коту или купить ему еды
        :param eaten_food: съеденная котом еда
        :param purchased_food: купленная коту еда
        """
        self.__cat_food += purchased_food - eaten_food

    def get_cat_food(self) -> int:
        return self.__cat_food

    def set_dirt(self, cleaning: int = 0, wallpaper: int = 0):
        """
        Изменить количество грязи в доме в зависимости от событий:
        кот ободрал обои или уборка в доме.
        :param cleaning: уборка грязи
        :param wallpaper: количество грязи от обоев
        """
        self.__dirt += wallpaper - cleaning

    def get_dirt(self) -> int:
        return self.__dirt


class Person(Home):
    """
    Дочерний класс параметров Жителя дома
    Args:
        name: имя
        name: имя
    Attributes:
        __happiness: счастье
        __satiety: сытость
    """

    __happiness: int = 100
    __name: str
    __satiety: int

    def __init__(self, name: str):
        self.__name = name
        self.__satiety = 30

    def get_name(self) -> str:
        return self.__name

    def set_satiety(self, meal: int = 0, action: int = 10):
        """
        Восполнить сытость едой или потратить её на действие
        :param meal: съеденная еда
        :param action: трата сытость на любое действие
        """
        self.__satiety += meal - action
        self.count_results_of_life(meal=meal)

    def get_satiety(self) -> int:
        return self.__satiety

    def set_happiness(
        self, fur_coat: int = 0, games: int = 0, cat: int = 0, dirt: bool = False
    ):
        """
        Изменить счастье в зависимости от событий: покупка шубы,
        игра в компьютерные игры, поглаживание кота или множество грязи
        :param fur_coat: счастье за шубу
        :param games: счастье за игры в ПК
        :param cat: счастье за поглаживание кота
        :param dirt: учёт грязи в доме
        уменьшение счастья за счёт большого количества грязи
        """
        self.__happiness += fur_coat + games + cat
        self.__happiness = self.__happiness if self.__happiness <= 100 else 100
        self.__happiness -= 10 if self.get_dirt() > 90 and dirt else 0

    def get_happiness(self) -> int:
        return self.__happiness

    def __str__(self):
        return f"{self.__name}:\n" f"Сытость: {self.__satiety}\n"


class Husband(Person):
    """
    Дочерний класс Мужа в доме
    """

    def eat(self, meal: int):
        """
        Поесть с учётом траты еды
        :param meal: съеденная мужем еда
        """
        self.set_satiety(meal=meal, action=0)
        self.set_food(eaten_food=meal)

    def work(self):
        """
        Заработать мужу деньги с учётом траты сытости
        """
        self.set_money(salary=150)
        self.count_results_of_life(salary=150)
        self.set_satiety()

    def play_games(self):
        """
        Поиграть в компьютер мужу с учётом траты сытости
        """
        self.set_happiness(games=20)
        self.set_satiety()

    def pet_cat(self):
        """
        Погладить кота мужу
        """
        self.set_happiness(cat=5)

    def __str__(self):
        return f"{super().__str__()}" f"Счастье: {self.get_happiness()}\n"


class Wife(Person):
    """
    Дочерний класс Жены в доме
    """

    def eat(self, meal: int):
        """
        Поесть жене с учётом траты еды
        :param meal: съеденная женой еда
        """
        self.set_satiety(meal=meal, action=0)
        self.set_food(eaten_food=meal)

    def go_to_shop(self, food: int = 0, cat_food: int = 0):
        """
        Пойти в магазин жене и купить продукты для людей и кота
        с учётом траты сытости и денег
        """
        self.set_money(food_cost=food, cat_food_cost=cat_food)
        self.set_food(purchased_food=food)
        self.set_cat_food(purchased_food=cat_food)
        self.set_satiety()

    def clean_up(self):
        """
        Провести уборку в доме с учётом траты сытости
        """
        self.set_dirt(cleaning=90)
        self.set_satiety()

    def buy_fur_coat(self):
        """
        Купить шубу с учётом траты сытости
        """
        self.set_money(fur_coat_cost=350)
        self.set_happiness(fur_coat=60)
        self.count_results_of_life(fur_coat=True)
        self.set_satiety()

    def pet_cat(self):
        """
        Погладить кота жене
        """
        self.set_happiness(cat=5)

    def __str__(self):
        return f"{super().__str__()}" f"Счастье: {self.get_happiness()}\n"


class Cat(Person):
    """
    Дочерний класс Кота в доме
    """

    def eat(self, meal: int):
        """
        Поесть коту с учётом траты кошачьего корма
        :param meal: съеденная еда
        """
        self.set_satiety(meal=2 * meal, action=0)
        self.set_cat_food(eaten_food=meal)

    def tear_wallpaper(self):
        """
        Ободрать обои с учётом траты сытости и образования дополнительной грязи
        """
        self.set_dirt(wallpaper=5)
        self.set_satiety()

    def sleep(self):
        """
        Спать коту с учётом траты сытости
        """
        self.set_satiety()

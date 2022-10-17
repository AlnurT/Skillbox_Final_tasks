import pytest
from Task_6.family_classes import Cat, Home, Husband, Wife


@pytest.fixture()
def home():
    return Home()


def test_count_results_of_life(home: Home):
    """
    Проверка подсчёта итогов жизни: количество заработанных денег,
    количество съеденной еды и число купленных шуб
    :param home: класс дома
    """
    home.count_results_of_life(salary=150, meal=30, fur_coat=True)
    assert (
        home.get_total_salary(),
        home.get_total_eaten_food(),
        home.get_number_of_fur_coat(),
    ) == (150, 30, 1)


@pytest.fixture()
def husband():
    return Husband(name="Alnur")


def test_eat_buy_husband(husband: Husband):
    """
    Проверка увеличения сытости мужа и уменьшения количества еды в доме после приёма пищи
    Начальная сытость: 30\n
    Начальная еда: 50
    :param husband: класс мужа
    """
    husband.eat(meal=30)
    assert (husband.get_satiety(), husband.get_food()) == (60, 20)


def test_work_by_husband(husband: Husband):
    """
    Проверка увеличения денег в доме и уменьшения сытости мужа после работы
    Начальные деньги: 100\n
    Начальная сытость: 30\n
    Зарплата: 150
    :param husband: класс мужа
    """
    husband.work()
    assert (husband.get_money(), husband.get_satiety()) == (250, 20)


@pytest.mark.parametrize(("happiness", "new_happiness"), [(100, 20), (0, 100)])
def test_play_games_by_husband(husband: Husband, happiness: int, new_happiness: int):
    """
    Проверка увеличения радости и уменьшения сытости мужа после игр
    Начальная радость: 100\n
    Начальная сытость: 30\n
    Счастье за игры: 20
    :param husband: класс мужа
    :param happiness: снижение счастья
    :param new_happiness: показатель счастья в зависимости от его максимального значения
    """
    husband.set_happiness(games=-happiness)
    husband.play_games()
    assert (husband.get_happiness(), husband.get_satiety()) == (new_happiness, 20)


@pytest.mark.parametrize(("happiness", "new_happiness"), [(100, 5), (0, 100)])
def test_pet_cat(husband: Husband, happiness: int, new_happiness: int):
    """
    Проверка увеличения радости после поглаживания кота
    Начальная радость: 100\n
    Счастье за кота: 5
    :param husband: класс мужа
    :param happiness: снижение счастья мужа
    :param new_happiness: показатель счастья мужа в зависимости
    от его максимального значения
    """
    husband.set_happiness(games=-happiness)
    husband.pet_cat()
    assert husband.get_happiness() == new_happiness


@pytest.fixture()
def wife():
    return Wife(name="Anna")


def test_eat_buy_wife(wife: Wife):
    """
    Проверка увеличения сытости жены и уменьшения количества еды в доме после приёма пищи
    Начальная сытость: 30\n
    Начальная еда: 50
    :param wife: класс жены
    """
    wife.eat(meal=30)
    assert (wife.get_satiety(), wife.get_food()) == (60, 20)


def test_go_to_shop_by_wife(wife: Wife):
    """
    Проверка уменьшения денег, увеличения еды и кошачьего корма, уменьшения сытости жены
    после похода в магазин
    Начальные деньги: 100\n
    Еда в холодильнике: 50\n
    Покупка еды: 60\n
    Кошачья еда: 30\n
    Покупка кошачьей еды: 10\n
    Начальная сытость: 30
    :param wife: класс жены
    """
    wife.go_to_shop(food=60, cat_food=10)
    assert (
        (wife.get_money(), wife.get_food(), wife.get_cat_food(), wife.get_satiety())
    ) == (30, 110, 40, 20)


def test_clean_up_by_wife(wife: Wife):
    """
    Проверка уменьшения грязи в доме и сытости жены после уборки
    Начальная грязь: 0\n
    Начальная сытость: 30
    :param wife: класс жены
    """
    wife.set_dirt(wallpaper=100)
    wife.clean_up()
    assert (wife.get_dirt(), wife.get_satiety()) == (10, 20)


@pytest.mark.parametrize(("happiness", "new_happiness"), [(100, 60), (0, 100)])
def test_buy_fur_coat_by_wife(wife: Wife, happiness: int, new_happiness: int):
    """
    Проверка уменьшения денег в доме, увеличения настроения и уменьшения сытости жены
    после покупки шубы
    Начальные деньги: 100\n
    Начальное счастье: 100\n
    Начальная сытость: 30
    :param wife: класс жены
    :param happiness: снижение счастья жены
    :param new_happiness: показатель счастья жены в зависимости
    от его максимального значения
    """
    wife.set_happiness(games=-happiness)
    wife.set_money(salary=400)
    wife.buy_fur_coat()
    assert (wife.get_money(), wife.get_happiness(), wife.get_satiety()) == (
        150,
        new_happiness,
        20,
    )


@pytest.fixture()
def cat():
    return Cat(name="Marsik")


def test_eat_by_cat(cat):
    """
    Проверка увеличения сытости кота и уменьшения корма в доме после приёма пищи
    Начальная сытость: 30\n
    Начальная еда: 30
    :param cat: класс кота
    """
    cat.eat(meal=10)
    assert (cat.get_satiety(), cat.get_cat_food()) == (50, 20)


def test_tear_wallpaper_by_cat(cat):
    """
    Проверка увеличения грязи в доме и уменьшения сытости кота после порчи обоев
    Начальная грязь: 0\n
    Начальная сытость: 30
    :param cat: класс кота
    """
    cat.tear_wallpaper()
    assert (cat.get_dirt(), cat.get_satiety()) == (5, 20)


def test_sleep_by_cat(cat):
    """
    Проверка уменьшения сытости кота после сна
    Начальная сытость: 30
    :param cat: класс кота
    """
    cat.sleep()
    assert cat.get_satiety() == 20

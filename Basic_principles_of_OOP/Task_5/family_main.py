"""Задача 6. Совместное проживание 2

Артём увлёкся предыдущим экспериментом и решил расширить его,
создав целую семью из Мужа, Жены и Кота. Условия эксперимента следующие.
Каждый день участники жизни могут делать только одно действие.
Все вместе они должны прожить год и не умереть.

Муж может:
- есть;
- играть;
- ходить на работу.

Жена может:
- есть;
- покупать продукты;
- покупать шубу;
- убираться в доме.
Кот может:
- есть;
- спать;
- драть обои.
Все они живут в одном доме, дом характеризуется:
- количеством денег в тумбочке (вначале 100);
- количеством еды в холодильнике (вначале 50);
- едой для кота (вначале 30);
- количеством грязи (вначале 0).
У людей есть имя, степень сытости (вначале 30) и степень счастья (вначале 100).
Все люди могут гладить кота (+5 к счастью).
У кота есть имя и степень сытости (вначале 30).
Любое действие (в том числе и кота), кроме «есть», приводит к уменьшению степени
сытости на 10 пунктов.
Взрослые едят максимум по 30 единиц еды, степень сытости растёт на один пункт
за один пункт еды.
Кот ест максимум по 10 единиц еды, степень сытости растёт на два пункта за один пункт еды.
Степень сытости не должна падать ниже нуля, иначе человек или кот умрёт от голода.
Деньги в тумбочку добавляет муж после работы — сразу 150 единиц.
Еда стоит 10 денег за 10 единиц еды. Шуба стоит 350 единиц.
Еда для кота тоже покупается — за 10 денег 10 еды.
Грязь добавляется каждый день по пять пунктов, за одну уборку жена может убирать
до 100 единиц грязи.
Если кот дерёт обои, то грязи тоже становится больше на пять пунктов.
Если в доме грязи больше 90, у людей падает степень счастья каждый день на 10 пунктов.
Степень счастья растёт: у мужа от игры в компьютер (на 20), у жены от покупки шубы
(на 60, но шуба дорогая).
Степень счастья не должна падать ниже 10, иначе человек умирает от депрессии.
Реализуйте такую программу. Подведите итоги жизни за год — сколько было заработано денег,
сколько съедено еды, сколько куплено шуб.
"""

from random import randint
from typing import Union

from Task_5.family_classes import Cat, Husband, Wife


def do_action_by_husband(husband: Husband):
    if husband.get_satiety() < 20:
        husband.eat(meal=randint(1, 30))
        print(f"{husband.get_name()} поел")
    elif husband.get_happiness() < 50:
        husband.play_games()
        print(f"{husband.get_name()} играл в ПК")
    else:
        husband.work()
        print(f"{husband.get_name()} работал")
        husband.pet_cat()
        print(f"{husband.get_name()} погладил кота")
    husband.set_happiness(dirt=True)


def do_action_by_wife(wife: Wife):
    if wife.get_satiety() < 20:
        wife.eat(meal=randint(1, 30))
        print(f"{wife.get_name()} поела")
    elif wife.get_food() < 120 < wife.get_money():
        wife.go_to_shop(food=120)
        print(f"{wife.get_name()} купила еду")
    elif wife.get_cat_food() < 20 < wife.get_money():
        wife.go_to_shop(cat_food=20)
        print(f"{wife.get_name()} купила корм")
    elif wife.get_dirt() > 90:
        print(f"{wife.get_name()} убралась в доме")
        wife.clean_up()
    elif wife.get_money() > 500:
        print(f"{wife.get_name()} купила шубу")
        wife.buy_fur_coat()
    else:
        wife.pet_cat()
        print(f"{wife.get_name()} погладила кота")
    wife.set_happiness(dirt=True)


def do_action_by_cat(cat: Cat):
    if cat.get_satiety() < 10:
        cat.eat(meal=randint(1, 10))
        print(f"{cat.get_name()} поел")
    elif randint(0, 1):
        cat.tear_wallpaper()
        print(f"{cat.get_name()} ободрал обои")
    else:
        cat.sleep()
        print(f"{cat.get_name()} спал")


def do_general_action(person: Union[Husband, Wife, Cat]) -> tuple:
    if person.get_satiety() < 0:
        print(f"{person.get_name()} умер от голода")
    elif person.get_happiness() < 10:
        print(f"{person.get_name()} умер от депрессии")
    elif isinstance(person, Husband):
        do_action_by_husband(person)
    elif isinstance(person, Wife):
        do_action_by_wife(person)
    else:
        do_action_by_cat(person)
    return (
        person.get_money(),
        person.get_food(),
        person.get_cat_food(),
        person.get_dirt(),
    )


def main():
    husband = Husband(name="Alnur")
    wife = Wife(name="Anna")
    cat = Cat(name="Marsik")
    family = (husband, wife, cat)
    money, food, cat_food, dirt = 100, 50, 30, 0
    total_salary, total_eaten_food, number_of_fur_coat = 0, 0, 0

    for day in range(1, 366):
        print(f"День {day}:")
        print(husband.get_parameters())

        for person in family:
            person.set_home_parameters(
                money=money, food=food, cat_food=cat_food, dirt=dirt
            )
            print(person)
            money, food, cat_food, dirt = do_general_action(person=person)
            print(person)

        dirt += 5
        for person in family:
            person.set_home_parameters(
                money=money, food=food, cat_food=cat_food, dirt=dirt
            )

        print(f"Прошёл {day} день и добавилось 5 грязи\n")

    for person in family:
        total_salary += person.get_total_salary()
        total_eaten_food += person.get_total_eaten_food()
        number_of_fur_coat += person.get_number_of_fur_coat()

    print(f"Денег заработано: {total_salary}")
    print(f"Еды съедено: {total_eaten_food}")
    print(f"Шуб куплено: {number_of_fur_coat}\n")


if __name__ == "__main__":
    main()

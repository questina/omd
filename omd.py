import random
from enum import Enum


class RainForce(Enum):
    SMALL_RAIN = 1
    MEDIUM_RAIN = 2
    LARGE_RAIN = 3


def step2_umbrella():
    """
    This function prints the end of the story
    if the duck would not take umbrella
    :return: None
    """
    print(
        'Утка решила взять зонт\n'
        'Хоть он ей и не понадобился, но '
        'оказалось что в баре проходит акция, '
        'в которой говорится, что если принести зонт '
        'в бар, то тебе подарят фирменную кружку.\n'
        'Уточка была рада случайному подарку и ее день '
        'прошел идеально!'
    )


def step2_no_umbrella():
    """
    This function computes the force of the rain
    and based on it continues the story of the duck
    if it would take umbrella
    :return: None
    """
    rain_force = random.choice(list(RainForce))
    if rain_force == RainForce.SMALL_RAIN:
        print(
            'Уточка решила не брать зонт, '
            'и ей повезло, потому что на улице '
            'шел совершенно незаметный дождь, '
            'который никак не помешал ей '
            'насладиться этим вечером!'
        )
    elif rain_force == RainForce.MEDIUM_RAIN:
        print(
            'Уточка решила не брать зонт, '
            'но когда она вышла из дома, '
            'то поняла, что на улице идет небольшой дождь.\n'
            '"Ну и ладно", подумала уточка, дождь же небольшой, '
            'я все равно смогу дойти до бара.\n'
            'Такие мысли согревали уточку и '
            'она быстренько добралась до бара, '
            'где насладилась этим вечером.'
        )
    else:
        print(
            'Уточка решила не брать зонт, '
            'но на улице оказался ужасный ливень.\n'
            'Уточка вспомнила, что она вообще-то водоплавающее '
            'и вода ей не страшна, и спокойно пошла в дождь до бара,\n'
            'успевая при этом купаться в больших лужах и удивлять прохожих.\n'
            'Этот вечер запомнился ей на всю жизнь!'
        )


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()

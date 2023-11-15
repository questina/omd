import random
from typing import Callable, Union
from functools import wraps

import click
from pizza import assortment, Pizza, Size


def log(arg: Union[Callable, str]) -> Callable:
    """
    Decorator, that prints into the stdout time of function
    process running. The time is generated via random.randint.

    The decorator can be used with or without parameter.
    If parameter is used, it needs to be a formatted string
    in which action time will be inserted. This string
    will be printed in stdout.
    If parameter is not used, the decorator will print
    the name of the function and it is time.
    :param arg: template string or function.
    :return: decorator.
    """
    if callable(arg):
        time_info_template = f'{arg.__name__} - {{}}s!'
    else:
        time_info_template = arg

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            action_time = random.randint(5, 20)
            res = func(*args, **kwargs)
            print(time_info_template.format(action_time))
            return res

        return wrapper

    if callable(arg):
        func = arg
        return decorator(func)
    return decorator


@log('‍🍳 Baked for {}m')
def bake(pizza: Pizza):
    """
    Writes in the output that pizza is being baked.
    :param pizza: type of pizza
    :return: None
    """
    print(f'⏲️ Started baking {pizza.name} size {pizza.size.value}...')


@log("🚴 Delivered in {}m")
def deliver(pizza: Pizza):
    """
    Writes in the output that pizza is being delivered.
    :param pizza: type of pizza
    :return: None
    """
    print(
        f'Your pizza {pizza.name} size {pizza.size.value} is ready! '
        f'Now arriving to you 🛵!'
    )


@log('🏠 Picked up in {}m')
def pickup(pizza: Pizza):
    """
    Writes in the output that pizza is ready for pickup.
    :param pizza: type of pizza
    :return: None
    """
    print(
        f'Your pizza {pizza.name} size {pizza.size.value} is ready! '
        f'Waiting for you ❤️'
    )


@click.group()
def launch() -> None:  # pragma: no cover
    pass


@launch.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option(
    '--size',
    default=Size.L.value,
    type=click.Choice([s.value for s in Size], case_sensitive=False)
)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool, size: str) -> None:
    """
    Place pizza order.
    After that pizza is being baked and then delivered or picked up.
    :param pizza: type of ordered pizza.
    :param delivery: flag if pizza needs to be delivered.
    :param size: pizza size, can be only L or XL.
    :return: None
    """
    pizza = pizza.lower()
    if pizza not in assortment:
        print(
            'Sorry, we do not have this type of pizza! Please check our menu'
        )
    else:
        cur_pizza = assortment[pizza](size=Size[size])
        bake(cur_pizza)
        if delivery:
            deliver(cur_pizza)
        else:
            pickup(cur_pizza)


@launch.command()
def menu() -> None:
    """
    Print menu of available pizzas.
    :return: None
    """
    for pizza in assortment.values():
        print(pizza())


if __name__ == '__main__':  # pragma: no cover
    launch()

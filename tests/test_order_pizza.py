from unittest.mock import patch
import pytest
from click.testing import CliRunner

from order_pizza import menu, order, bake, deliver, pickup, log
from pizza import Margherita, Pepperoni, Hawaiian

RANDOMINT = 2


@patch('builtins.print')
def test_menu(mocked_print):
    runner = CliRunner()
    runner.invoke(menu)
    correct_args = (Margherita(), Pepperoni(), Hawaiian())
    assert mocked_print.call_count == len(correct_args)
    for i, called_args in enumerate(mocked_print.call_args_list):
        assert called_args.args[0] == correct_args[i]


@pytest.mark.parametrize(
    'pizza_type,pizza_size,is_delivery',
    [
        ('margherita', 'XL', True),
        ('pepperoni', 'L', False),
    ]
)
@patch('random.randint', return_value=RANDOMINT)
@patch('builtins.print')
def test_correct_order(
    mocked_print, mocked_random, pizza_type, pizza_size, is_delivery
):
    runner = CliRunner()
    command_line_args = f'{pizza_type} --size {pizza_size}'
    if is_delivery:
        command_line_args += ' --delivery'
    runner.invoke(order, command_line_args)
    correct_args = [
        f'⏲️ Started baking {pizza_type.capitalize()} size {pizza_size}...',
        f'‍🍳 Baked for {RANDOMINT}m',
    ]
    if is_delivery:
        correct_args += [
            f'Your pizza {pizza_type.capitalize()} size '
            f'{pizza_size} is ready! Now arriving to you 🛵!',

            f'🚴 Delivered in {RANDOMINT}m'
        ]
    else:
        correct_args += [
            f'Your pizza {pizza_type.capitalize()} size '
            f'{pizza_size} is ready! Waiting for you ❤️',

            f'🏠 Picked up in {RANDOMINT}m'
        ]
    for i, called_args in enumerate(mocked_print.call_args_list):
        assert called_args.args[0] == correct_args[i]


@patch('builtins.print')
def test_incorrect_order(mocked_print):
    runner = CliRunner()
    runner.invoke(order, 'some_pizza --delivery')
    assert mocked_print.call_count == 1
    assert (
        mocked_print.call_args_list[0].args[0] ==
        'Sorry, we do not have this type of pizza! Please check our menu'
    )


@pytest.mark.parametrize(
    'func,printed_str',
    [
        (
            bake,
            '⏲️ Started baking Margherita size L...',
        ),
        (
            deliver,
            'Your pizza Margherita size L is ready! Now arriving to you 🛵!',
        ),
        (
            pickup,
            'Your pizza Margherita size L is ready! Waiting for you ❤️',
        )
    ]
)
@patch('builtins.print')
def test_bake(mocked_print, func, printed_str):
    base_func = func.__wrapped__
    base_func(Margherita())
    assert mocked_print.call_count == 1
    assert (
        mocked_print.call_args_list[0].args[0] ==
        printed_str
    )


@patch('random.randint', return_value=RANDOMINT)
@patch('builtins.print')
def test_log_decorator_without_params(mocked_print, mocked_random):
    @log
    def func():
        pass

    func()
    assert mocked_print.call_count == 1
    assert (
        mocked_print.call_args_list[0].args[0] ==
        f'func - {RANDOMINT}s!'
    )

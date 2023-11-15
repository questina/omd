import pytest

from pizza import Margherita, Pepperoni, Hawaiian, Pizza, Size


class ClassForTesting(Pizza):
    @property
    def ingredients(self):
        return ['a', 'b', 'c']

    @property
    def menu_emoji(self):
        return 'emoji'


class AnotherClassForTesting(Pizza):
    @property
    def ingredients(self):
        return ['b', 'c', 'd']

    @property
    def menu_emoji(self):
        return 'emoji'


def test_base_class_size():
    assert ClassForTesting().size == Size.L
    assert ClassForTesting(size=Size.L).size == Size.L
    assert ClassForTesting(size=Size.XL).size == Size.XL


def test_base_class_recipe():
    assert ClassForTesting().recipe == [
        'Make dough',
        'Add a',
        'Add b',
        'Add c',
        'Bake in oven for 20 min'
    ]


def test_base_class_dict():
    assert ClassForTesting().dict() == {
        1: 'Make dough',
        2: 'Add a',
        3: 'Add b',
        4: 'Add c',
        5: 'Bake in oven for 20 min'
    }


def test_base_class_str():
    assert str(ClassForTesting()) == 'ClassForTesting emoji: a, b, c'


def test_base_class_eq():
    assert ClassForTesting() == ClassForTesting()
    assert not (ClassForTesting() == AnotherClassForTesting())
    assert not (ClassForTesting() == ClassForTesting(size=Size.XL))


@pytest.mark.parametrize(
    'pizza_class,name,ingredients,menu_emoji',
    [
        (
            Margherita, 'Margherita',
            ['tomato sauce', 'mozzarella', 'tomatoes'], '🧀'
        ),
        (
            Pepperoni, 'Pepperoni',
            ['tomato sauce', 'mozzarella', 'pepperoni'], '🍕'
        ),
        (
            Hawaiian, 'Hawaiian',
            ['tomato sauce', 'mozzarella', 'chicken', 'pineapples'], '🍍'
        ),
    ]
)
def test_pizza_class(pizza_class, name, ingredients, menu_emoji):
    pizza = pizza_class()
    assert pizza.name == name
    assert pizza.ingredients == ingredients
    assert pizza.menu_emoji == menu_emoji

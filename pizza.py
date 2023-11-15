from abc import abstractmethod, ABC
from enum import Enum
from typing import List, Dict, Type


class Size(Enum):
    XL = 'XL'
    L = 'L'


class Pizza(ABC):
    """
    This is an abstract class for storing information about pizza.

    Attributes:
    ------------
    size: str
        Size of pizza. Can only be L or XL.
    name: str
        Name of pizza. Class name by default.
    ingredients: list
        Pizza ingredients.
    menu_emoji: str
        Emoji that will be displayed on the menu.
    recipe: list
        Steps on how to make pizza.
    """

    def __init__(self, size: Size = Size.L):
        self.size = size
        self.name = self.__class__.__name__

    @property
    @abstractmethod
    def ingredients(self) -> List[str]:
        """
        List of pizza ingredients.
        :return: pizza ingredients.
        """

    @property
    @abstractmethod
    def menu_emoji(self) -> str:
        """
        Emoji that will be displayed on the menu.
        :return: menu emoji.
        """

    @property
    def recipe(self) -> List[str]:
        """
        Steps on how to make pizza.
        :return: list of recipe steps.
        """
        return (
            ['Make dough']
            + [f'Add {ingredient}' for ingredient in self.ingredients]
            + ['Bake in oven for 20 min']
        )

    def dict(self) -> Dict[int, str]:
        """
        Steps on how to make pizza in a format
        {step number: step explanation}.
        :return: recipe steps.
        """
        return dict(enumerate(self.recipe, start=1))

    def __eq__(self, other) -> bool:
        """
        Compare two classes by their ingredients and sizes.
        :param other: another pizza class to compare with.
        :return: true if pizzas identical else false.
        """
        if (
            self.size == other.size
            and self.ingredients == other.ingredients
        ):
            return True
        return False

    def __str__(self) -> str:
        """
        Transform pizza description in string.
        :return: pizza description.
        """
        return f'{self.name} {self.menu_emoji}: {", ".join(self.ingredients)}'


class Margherita(Pizza):
    @property
    def ingredients(self) -> List[str]:
        """
        List of pizza ingredients.
        :return: pizza ingredients.
        """
        return ['tomato sauce', 'mozzarella', 'tomatoes']

    @property
    def menu_emoji(self) -> str:
        """
        Emoji that will be displayed on the menu.
        :return: menu emoji.
        """
        return '🧀'


class Pepperoni(Pizza):
    @property
    def ingredients(self) -> List[str]:
        """
        List of pizza ingredients.
        :return: pizza ingredients.
        """
        return ['tomato sauce', 'mozzarella', 'pepperoni']

    @property
    def menu_emoji(self) -> str:
        """
        Emoji that will be displayed on the menu.
        :return: menu emoji.
        """
        return '🍕'


class Hawaiian(Pizza):
    @property
    def ingredients(self) -> List[str]:
        """
        List of pizza ingredients.
        :return: pizza ingredients.
        """
        return ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']

    @property
    def menu_emoji(self) -> str:
        """
        Emoji that will be displayed on the menu.
        :return: menu emoji.
        """
        return '🍍'


assortment: Dict[str, Type[Pizza]] = {
    'margherita': Margherita,
    'pepperoni': Pepperoni,
    'hawaiian': Hawaiian,
}

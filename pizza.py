# pizza.py
from typing import Dict, List


class Pizza:
    def __init__(self, name: str, ingredients: List[str], size: str = "L"):
        self.name = name
        self.ingredients = ingredients
        self.size = size

    def dict(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "ingredients": ", ".join(self.ingredients),
            "size": self.size
        }

    def __eq__(self, other):
        if not isinstance(other, Pizza):
            return NotImplemented
        return ((self.name, self.ingredients, self.size)
                == (other.name, other.ingredients, other.size))

    def __str__(self):
        return (f"{self.name} Pizza: " + ", ".join(self.ingredients)
                + f" ({self.size})")


class Margherita(Pizza):
    def __init__(self, size: str = "L"):
        super().__init__("Margherita", [
            "tomato sauce", "mozzarella", "tomatoes"], size)


class Pepperoni(Pizza):
    def __init__(self, size: str = "L"):
        super().__init__("Pepperoni", [
            "tomato sauce", "mozzarella", "pepperoni"], size)


class Hawaiian(Pizza):
    def __init__(self, size: str = "L"):
        super().__init__("Hawaiian", [
            "tomato sauce", "mozzarella", "chicken", "pineapples"], size)

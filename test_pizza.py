# test_pizza.py
import unittest
from unittest.mock import patch
from pizza import Margherita, Pepperoni, Hawaiian
from decorators import log


class TestPizza(unittest.TestCase):
    # Тестирование ингредиентов пиццы Маргарита
    def test_margherita_ingredients(self):
        pizza = Margherita()
        self.assertIn("tomatoes", pizza.ingredients,
                      "В пицце Маргарита должны быть помидоры")

    # Тестирование размера пиццы Пепперони
    def test_pepperoni_size(self):
        pizza = Pepperoni(size="XL")
        self.assertEqual(pizza.size, "XL",
                         "Размер пиццы Пепперони должен быть XL")

    # Тестирование сравнения двух одинаковых пицц Гавайской
    def test_hawaiian_equality(self):
        pizza1 = Hawaiian()
        pizza2 = Hawaiian()
        self.assertEqual(
            pizza1, pizza2, "Две одинаковые Гавайские пиццы должны быть равны")

    # Тестирование декоратора логирования
    def test_log_decorator(self):
        @log('Тестовое сообщение: {}с!')
        def fake_function():
            pass

        with patch('builtins.print') as mock_print:
            fake_function()
            self.assertTrue(
                mock_print.called,
                "Декоратор логирования должен вызвать функцию print")


if __name__ == '__main__':
    unittest.main()

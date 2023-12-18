# cli.py
import click
from pizza import Margherita, Pepperoni, Hawaiian
from decorators import log


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', is_flag=True, default=False)
@click.argument('pizza_type', nargs=1)
def order(pizza_type: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    pizza_classes = {"margherita": Margherita,
                     "pepperoni": Pepperoni, "hawaiian": Hawaiian}

    if (pizza_type.lower() in pizza_classes):
        pizza = pizza_classes.get(pizza_type.lower())()
        bake(pizza)
        if delivery:
            deliver(pizza)
        else:
            pickup(pizza)
    else:
        print("Извините, такой пиццы нет. Выберите пиццу из меню)")


@cli.command()
def menu():
    """Выводит меню"""
    print(f"-🧀{Margherita()}")
    print(f"-🍕{Pepperoni()}")
    print(f"-🍍{Pepperoni()}")


@log("🧑‍🍳 Приготовили за {}с!")
def bake(pizza):
    """Готовит пиццу"""
    pass


@log("🛵 Доставили за {}с! Приятного аппетита!")
def deliver(pizza):
    """Доставляет пиццу"""
    pass


@log("🏠 Забрали за {}с!")
def pickup(pizza):
    """Самовывоз"""
    print(f"✅ Ваша пицца {pizza.name} готова к самовывозу!")


if __name__ == '__main__':
    cli()

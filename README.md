# AAA_Final_Project
Avito Analytics Academy final Python project 

## Основной функционал

- **Заказ пиццы**: Пользователи могут заказать любую пиццу из меню. Доступны варианты с доставкой и без.
- **Просмотр меню**: Вывод списка всех доступных пицц.
- **Логирование**: Отслеживание времени приготовления и доставки (или самовывоза) пиццы.

## Установка

Убедитесь, что у вас установлен Python версии 3.x. Для работы приложения требуется пакет `click`.


## Использование

### Просмотр меню

Чтобы просмотреть меню, выполните:

```bash
python cli.py menu
```

### Заказ пиццы

Для заказа пиццы используйте команду:

```bash
python cli.py order [название пиццы] [--delivery]
```

- Используйте `--delivery` для заказа с доставкой.
- Опустите `--delivery` для самовывоза.

### Примеры команд

```bash
python cli.py order Margherita --delivery
python cli.py order Pepperoni
```

## Тестирование

Проект включает тесты для проверки корректности работы функций и классов.

Чтобы запустить тесты, выполните:

```bash
python test_pizza.py
```

Это запустит все юнит-тесты, включенные в проект.

## Разработка

Проект состоит из следующих основных файлов:

- `pizza.py`: Классы пицц с их рецептами и методами.
- `cli.py`: Команды интерфейса командной строки для взаимодействия с пользователем.
- `decorators.py`: Декораторы для логирования времени выполнения функций.
- `test_pizza.py`: Тесты для проверки функционала пицц и декораторов.
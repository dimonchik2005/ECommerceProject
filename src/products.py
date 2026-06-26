from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""

    @abstractmethod
    def __add__(self, other: "Product") -> float:
        """Складывает продукты."""


class PrintMixin:
    """Миксин для вывода информации о создании объекта."""

    def __init__(self) -> None:
        """Выводит информацию о созданном объекте."""
        print(repr(self))
        super().__init__()


class Product(PrintMixin, BaseProduct):
    """Класс для описания товара."""

    name: str
    description: str
    quantity: int

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        """Инициализирует объект товара."""
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __repr__(self) -> str:
        """Возвращает техническое строковое представление объекта."""
        return (
            f"{type(self).__name__}("
            f"{self.name!r}, "
            f"{self.description!r}, "
            f"{self.price}, "
            f"{self.quantity}"
            f")"
        )

    def __str__(self) -> str:
        """Возвращает строковое представление товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Возвращает общую стоимость товаров одного класса."""
        if type(self) is not type(other):
            raise TypeError("Складывать можно только товары одного класса")

        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product_data: dict[str, Any]) -> "Product":
        """Создает новый объект Product из словаря."""
        return cls(
            product_data["name"],
            product_data["description"],
            float(product_data["price"]),
            int(product_data["quantity"]),
        )

    @property
    def price(self) -> float:
        """Возвращает цену товара."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливает новую цену товара."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        self.__price = new_price


class Smartphone(Product):
    """Класс для описания смартфона."""

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициализирует объект смартфона."""
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        """Возвращает техническое строковое представление смартфона."""
        return (
            f"{type(self).__name__}("
            f"{self.name!r}, "
            f"{self.description!r}, "
            f"{self.price}, "
            f"{self.quantity}, "
            f"{self.efficiency}, "
            f"{self.model!r}, "
            f"{self.memory}, "
            f"{self.color!r}"
            f")"
        )


class LawnGrass(Product):
    """Класс для описания газонной травы."""

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициализирует объект газонной травы."""
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        """Возвращает техническое строковое представление газонной травы."""
        return (
            f"{type(self).__name__}("
            f"{self.name!r}, "
            f"{self.description!r}, "
            f"{self.price}, "
            f"{self.quantity}, "
            f"{self.country!r}, "
            f"{self.germination_period!r}, "
            f"{self.color!r}"
            f")"
        )


class Category:
    """Класс для описания категории товаров."""

    category_count = 0
    product_count = 0

    name: str
    description: str

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        """Инициализирует объект категории."""
        self.name = name
        self.description = description
        self.__products: list[Product] = []

        Category.category_count += 1

        for product in products:
            self.add_product(product)

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        total_quantity = 0

        for product in self.__products:
            total_quantity += product.quantity

        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def middle_price(self) -> float:
        """Возвращает средний ценник товаров в категории."""
        try:
            return sum(product.price for product in self.__products) / len(
                self.__products
            )
        except ZeroDivisionError:
            return 0

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product и его наследников")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает список товаров категории в виде строки."""
        result = ""

        for product in self.__products:
            result += f"{product}\n"

        return result

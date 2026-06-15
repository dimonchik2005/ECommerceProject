from typing import Any


class Product:
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
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Возвращает строковое представление товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Возвращает общую стоимость двух товаров на складе."""
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
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        total_quantity = 0

        for product in self.__products:
            total_quantity += product.quantity

        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает список товаров категории в виде строки."""
        result = ""

        for product in self.__products:
            result += f"{product}\n"

        return result

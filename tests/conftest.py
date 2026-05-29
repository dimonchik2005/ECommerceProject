import pytest

from src.products import Category, Product


@pytest.fixture(autouse=True)
def reset_category_counts() -> None:
    """Сбрасывает счетчики Category перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def product() -> Product:
    """Возвращает тестовый товар."""
    return Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )


@pytest.fixture
def product2() -> Product:
    """Возвращает второй тестовый товар."""
    return Product(
        "Iphone 17",
        "512GB, Gray space",
        210000.0,
        8,
    )


@pytest.fixture
def category(product: Product, product2: Product) -> Category:
    """Возвращает тестовую категорию."""
    return Category(
        "Смартфоны",
        "Смартфоны для повседневного использования",
        [product, product2],
    )

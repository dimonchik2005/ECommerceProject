import pytest

from src.products import Category, LawnGrass, Product, Smartphone


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
        "Iphone 15",
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


@pytest.fixture
def smartphone() -> Smartphone:
    """Возвращает тестовый смартфон."""
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def smartphone2() -> Smartphone:
    """Возвращает второй тестовый смартфон."""
    return Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space",
    )


@pytest.fixture
def lawn_grass() -> LawnGrass:
    """Возвращает тестовую газонную траву."""
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

from src.products import Category, Product


def test_product_initialization(product: Product) -> None:
    """Проверяет корректность инициализации Product."""

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_initialization(
    category: Category, product: Product, product2: Product
) -> None:
    """Проверяет корректность инициализации Category."""

    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны для повседневного использования"
    assert category.products == [product, product2]


def test_category_count(product: Product) -> None:
    """Проверяет подсчёт количества категорий."""
    Category("Смартфоны", "Описание", [product])
    Category("Телевизоры", "Описание", [product])

    assert Category.category_count == 2


def test_product_count(product: Product, product2: Product) -> None:
    """Проверяет подсчёт количества товаров."""
    Category("Смартфоны", "Описание", [product, product2])
    Category("Телевизоры", "Описание", [product])

    assert Category.product_count == 3


def test_empty_category_products_count() -> None:
    """Проверяет категорию без товаров."""
    category = Category("Пустая категория", "Описание", [])

    assert category.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0

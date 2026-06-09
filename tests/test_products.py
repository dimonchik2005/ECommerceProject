from src.products import Category, Product


def test_product_initialization(product: Product) -> None:
    """Проверяет корректность инициализации Product."""
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_initialization(
    category: Category,
) -> None:
    """Проверяет корректность инициализации Category."""
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны для повседневного использования"


def test_category_products_property(category: Category) -> None:
    """Проверяет геттер products."""
    assert category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_add_product(category: Category) -> None:
    """Проверяет добавление продукта в категорию."""
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category.add_product(product)

    assert "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n" in category.products
    assert Category.product_count == 3


def test_category_count(product: Product) -> None:
    """Проверяет подсчет количества категорий."""
    Category("Смартфоны", "Описание", [product])
    Category("Телевизоры", "Описание", [product])

    assert Category.category_count == 2


def test_product_count(product: Product, product2: Product) -> None:
    """Проверяет подсчет количества товаров."""
    Category("Смартфоны", "Описание", [product, product2])
    Category("Телевизоры", "Описание", [product])

    assert Category.product_count == 3


def test_empty_category_products_count() -> None:
    """Проверяет категорию без товаров."""
    category = Category("Пустая категория", "Описание", [])

    assert category.products == ""
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_new_product() -> None:
    """Проверяет создание продукта через класс-метод."""
    product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }

    product = Product.new_product(product_data)

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_price_setter_positive(product: Product) -> None:
    """Проверяет установку положительной цены."""
    product.price = 200000.0

    assert product.price == 200000.0


def test_product_price_setter_negative(product: Product, capsys) -> None:
    """Проверяет запрет установки отрицательной цены."""
    product.price = -100
    captured = capsys.readouterr()

    assert product.price == 180000.0
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_price_setter_zero(product: Product, capsys) -> None:
    """Проверяет запрет установки нулевой цены."""
    product.price = 0
    captured = capsys.readouterr()

    assert product.price == 180000.0
    assert "Цена не должна быть нулевая или отрицательная" in captured.out

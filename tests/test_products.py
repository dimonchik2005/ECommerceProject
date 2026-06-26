import pytest

from src.products import BaseProduct, Category, LawnGrass, Product, Smartphone


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


def test_product_str(product: Product) -> None:
    """Проверяет строковое представление товара."""
    assert str(product) == ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.")


def test_category_str(category: Category) -> None:
    """Проверяет строковое представление категории."""
    assert str(category) == "Смартфоны, количество продуктов: 13 шт."


def test_product_add(product: Product, product2: Product) -> None:
    """Проверяет сложение товаров."""
    assert product + product2 == 2580000.0


def test_smartphone_initialization(smartphone: Smartphone) -> None:
    """Проверяет создание объекта Smartphone."""
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_lawn_grass_initialization(lawn_grass: LawnGrass) -> None:
    """Проверяет создание объекта LawnGrass."""
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Элитная трава для газона"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зеленый"


def test_add_same_product_class(
    smartphone: Smartphone,
    smartphone2: Smartphone,
) -> None:
    """Проверяет сложение товаров одного класса."""
    assert smartphone + smartphone2 == 2580000.0


def test_add_different_product_classes(
    smartphone: Smartphone,
    lawn_grass: LawnGrass,
) -> None:
    """Проверяет запрет сложения товаров разных классов."""
    with pytest.raises(TypeError):
        smartphone + lawn_grass


def test_add_product_inherited_class(smartphone: Smartphone) -> None:
    """Проверяет добавление наследника Product в категорию."""
    category = Category("Смартфоны", "Описание", [])

    category.add_product(smartphone)

    assert "Samsung Galaxy S23 Ultra" in category.products
    assert Category.product_count == 1


def test_add_product_wrong_type(category: Category) -> None:
    """Проверяет запрет добавления объекта не Product."""
    with pytest.raises(TypeError):
        category.add_product("Not a product")  # type: ignore[arg-type]


def test_base_product_is_abstract() -> None:
    """Проверяет, что BaseProduct является абстрактным классом."""
    with pytest.raises(TypeError):
        BaseProduct()  # type: ignore[abstract]


def test_product_mixin_print(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверяет вывод миксина при создании Product."""
    Product("Test product", "Test description", 100.0, 2)
    captured = capsys.readouterr()

    assert "Product('Test product', 'Test description', 100.0, 2)" in captured.out


def test_smartphone_mixin_print(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверяет вывод миксина при создании Smartphone."""
    Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    captured = capsys.readouterr()

    assert (
        "Smartphone('Samsung Galaxy S23 Ultra', "
        "'256GB, Серый цвет, 200MP камера', "
        "180000.0, 5, 95.5, 'S23 Ultra', 256, 'Серый')"
    ) in captured.out


def test_lawn_grass_mixin_print(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверяет вывод миксина при создании LawnGrass."""
    LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    captured = capsys.readouterr()

    assert (
        "LawnGrass('Газонная трава', "
        "'Элитная трава для газона', "
        "500.0, 20, 'Россия', '7 дней', 'Зеленый')"
    ) in captured.out


def test_product_zero_quantity() -> None:
    """Проверяет запрет создания товара с нулевым количеством."""
    with pytest.raises(
        ValueError,
        match="Товар с нулевым количеством не может быть добавлен",
    ):
        Product("Test product", "Test description", 100.0, 0)


def test_category_middle_price(category: Category) -> None:
    """Проверяет расчет среднего ценника товаров категории."""
    assert category.middle_price() == 195000.0


def test_category_middle_price_empty() -> None:
    """Проверяет средний ценник пустой категории."""
    category = Category("Пустая категория", "Описание", [])

    assert category.middle_price() == 0

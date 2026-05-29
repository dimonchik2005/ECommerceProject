import json
from unittest.mock import mock_open, patch

from src.products import Category
from src.utils import create_categories_from_json, read_json_file


def test_read_json_file() -> None:
    """Проверяет чтение JSON-файла."""
    data = [
        {
            "name": "Смартфоны",
            "description": "Описание",
            "products": [],
        }
    ]

    with patch("builtins.open", mock_open(read_data=json.dumps(data))):
        result = read_json_file("data/products.json")

    assert result == data


def test_read_json_file_not_found() -> None:
    """Проверяет чтение отсутствующего JSON-файла."""
    result = read_json_file("missing.json")

    assert result == []


def test_read_json_file_invalid_json() -> None:
    """Проверяет обработку некорректного JSON."""
    with patch("builtins.open", mock_open(read_data="invalid json")):
        result = read_json_file("data/products.json")

    assert result == []


def test_read_json_file_not_list() -> None:
    """Проверяет обработку JSON, который не является списком."""
    with patch("builtins.open", mock_open(read_data=json.dumps({"name": "test"}))):
        result = read_json_file("data/products.json")

    assert result == []


def test_create_categories_from_json() -> None:
    """Проверяет создание объектов Category из JSON."""
    categories = create_categories_from_json("data/products.json")

    assert len(categories) == 2
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 3
    assert categories[0].products[0].name == "Samsung Galaxy C23 Ultra"
    assert categories[1].name == "Телевизоры"
    assert len(categories[1].products) == 1
    assert Category.category_count == 2
    assert Category.product_count == 4

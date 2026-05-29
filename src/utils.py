import json
from typing import Any

from src.products import Category, Product


def read_json_file(file_path: str) -> list[dict[str, Any]]:
    """Считывает JSON-файл и возвращает список словарей."""

    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError, json.JSONDecodeError:
        return []

    if not isinstance(data, list):
        return []

    return data


def create_categories_from_json(file_path: str) -> list[Category]:
    """Создает список объектов Category из JSON-файла."""

    categories_data = read_json_file(file_path)
    categories = []

    for category_data in categories_data:
        products = [
            Product(
                product_data["name"],
                product_data["description"],
                float(product_data["price"]),
                int(product_data["quantity"]),
            )
            for product_data in category_data.get("products", [])
        ]

        category = Category(
            category_data["name"],
            category_data["description"],
            products,
        )
        categories.append(category)

    return categories

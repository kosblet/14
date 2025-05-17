# tests/test_main.py

import pytest
from ecommerce.main import Product, Category


def test_product_initialization():
    product = Product("Test", "Test Description", 100.0, 10)
    assert product.name == "Test"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_private_price_property_and_setter():
    product = Product("Test", "Test", 100.0, 10)
    assert product.price == 100.0

    product.price = 90.0
    assert product.price == 90.0

    with pytest.raises(ValueError):
        product.price = -100.0

    with pytest.raises(ValueError):
        product.price = 0.0


def test_new_product_classmethod():
    data = {
        "name": "Новый продукт",
        "description": "Описание",
        "price": 200.0,
        "quantity": 15
    }

    # Сброс счётчиков
    Category.category_count = 0
    Category.product_count = 0

    product = Product.new_product(data)
    assert product.name == "Новый продукт"
    assert product.price == 200.0
    assert product.quantity == 15

    updated = Product.new_product(data, [product])
    assert updated.quantity == 30  # 15 + 15
    assert updated.price == 200.0


def test_add_product_method():
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("P1", "Desc1", 100.0, 10)
    category = Category("Электроника", "Описание", [])
    category.add_product(product1)

    assert len(category.products.split("\n")) == 2
    assert Category.product_count == 1

    with pytest.raises(TypeError):
        category.add_product("Не продукт")


def test_category_products_property():
    product1 = Product("P1", "Desc1", 100.0, 10)
    product2 = Product("P2", "Desc2", 200.0, 5)
    category = Category("Электроника", "Описание", [product1, product2])

    expected = (
        "P1, 100.0 руб. Остаток: 10 шт.\n"
        "P2, 200.0 руб. Остаток: 5 шт.\n"
    )
    assert category.products == expected


def test_category_counters():
    # Сброс счётчиков
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("P1", "Desc1", 100.0, 10)
    product2 = Product("P2", "Desc2", 200.0, 5)
    product3 = Product("P3", "Desc3", 300.0, 15)

    category1 = Category("Электроника", "Описание", [product1, product2])
    category2 = Category("Другое", "Ещё описание", [product3])

    assert Category.category_count == 2
    assert Category.product_count == 3  # количество объектов Product
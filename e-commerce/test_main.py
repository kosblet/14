import pytest
from main import Product, Category


# Тесты для класса Product
def test_product_initialization():
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


# Тесты для класса Category
def test_category_initialization():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category(
        "Смартфоны", "Смартфоны как средство коммуникации", [product1, product2]
    )

    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны как средство коммуникации"
    assert len(category.products) == 2


# Тесты для счетчиков категорий и продуктов
def test_category_counters():
    # Сбросим счетчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны", "Смартфоны как средство коммуникации", [product1, product2]
    )
    category2 = Category("Телевизоры", "Современные телевизоры", [product3])

    assert Category.category_count == 2
    assert Category.product_count == 3


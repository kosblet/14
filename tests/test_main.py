import pytest
from ecommerce import Product, Category


def test_product_str():
    product = Product("Test", "Test Description", 100.0, 5)
    assert str(product) == "Test, 100.0 руб. Остаток: 5 шт."


def test_category_str():
    product1 = Product("P1", "Desc1", 100.0, 10)
    product2 = Product("P2", "Desc2", 200.0, 5)
    category = Category("Электроника", "Описание", [product1, product2])
    assert str(category) == "Электроника, количество продуктов: 15 шт."


def test_product_add():
    product1 = Product("P1", "Desc1", 100.0, 10)
    product2 = Product("P2", "Desc2", 200.0, 5)
    assert product1 + product2 == 100.0 * 10 + 200.0 * 5  # 1000 + 1000 = 2000.0

    with pytest.raises(TypeError):
        product1 + object()  # Нельзя сложить с другим типом


def test_category_products_property():
    product1 = Product("P1", "Desc1", 100.0, 10)
    product2 = Product("P2", "Desc2", 200.0, 5)
    category = Category("Электроника", "Описание", [product1, product2])

    expected = (
        "P1, 100.0 руб. Остаток: 10 шт.\n"
        "P2, 200.0 руб. Остаток: 5 шт.\n"
    )
    assert category.products == expected
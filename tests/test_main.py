import pytest
from ecommerce.main import Product, Category

def test_product_creation_with_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Invalid Product", "Description", 1000.0, 0)

def test_product_creation():
    product = Product("Test Product", "Description", 100.0, 5)
    assert product.name == "Test Product"
    assert product.description == "Description"
    assert product.price == 100.0
    assert product.quantity == 5

def test_category_middle_price():
    product1 = Product("Product A", "Description A", 100.0, 5)
    product2 = Product("Product B", "Description B", 200.0, 10)
    product3 = Product("Product C", "Description C", 300.0, 15)

    category = Category("Test Category", "Description", [product1, product2, product3])
    assert category.middle_price() == 200.0  # (100 + 200 + 300) / 3

def test_category_middle_price_empty():
    category = Category("Empty Category", "No products", [])
    assert category.middle_price() == 0
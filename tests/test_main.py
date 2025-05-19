import pytest
from ecommerce.main import Product, Smartphone, LawnGrass

def test_product_creation():
    product = Product("Test Product", "Description", 100.0, 5)
    assert product.name == "Test Product"
    assert product.description == "Description"
    assert product.price == 100.0
    assert product.quantity == 5

def test_smartphone_creation():
    smartphone = Smartphone("Test Phone", "Description", 500.0, 10, 6.5, 6)
    assert smartphone.name == "Test Phone"
    assert smartphone.description == "Description"
    assert smartphone.price == 500.0
    assert smartphone.quantity == 10
    assert smartphone.screen_size == 6.5
    assert smartphone.ram == 6

def test_lawn_grass_creation():
    grass = LawnGrass("Test Grass", "Description", 200.0, 20, "Green", "USA")
    assert grass.name == "Test Grass"
    assert grass.description == "Description"
    assert grass.price == 200.0
    assert grass.quantity == 20
    assert grass.color == "Green"
    assert grass.country_of_origin == "USA"

def test_display_info(capsys):
    product = Product("Test Product", "Description", 100.0, 5)
    product.display_info()
    captured = capsys.readouterr()
    assert "Product: Test Product" in captured.out
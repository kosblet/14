import pytest
from ecommerce.main import Product, Category, Smartphone, LawnGrass

def test_product_creation_with_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Invalid Product", "Description", 1000.0, 0)

def test_product_creation():
    product = Product("Test Product", "Description", 100.0, 5)
    assert product.name == "Test Product"
    assert product.description == "Description"
    assert product.price == 100.0
    assert product.quantity == 5

def test_smartphone_inheritance():
    sp = Smartphone("iPhone", "Best phone", 100000.0, 10, 98.5, "Pro", 512, "Черный")
    assert isinstance(sp, Product)
    assert sp.efficiency == 98.5
    assert sp.model == "Pro"
    assert sp.memory == 512
    assert sp.color == "Черный"

def test_lawn_grass_inheritance():
    lg = LawnGrass("Trava", "Good lawn", 100.0, 50, "Россия", "7 дней", "Зеленый")
    assert isinstance(lg, Product)
    assert lg.country == "Россия"
    assert lg.germination_period == "7 дней"
    assert lg.color == "Зеленый"

def test_add_smartphone():
    sp1 = Smartphone("iPhone", "Best phone", 100000.0, 10, 98.5, "Pro", 512, "Черный")
    sp2 = Smartphone("Xiaomi", "Budget phone", 30000.0, 20, 90.0, "Redmi", 128, "Серый")
    assert sp1 + sp2 == 100000.0 * 10 + 30000.0 * 20

def test_add_lawn_grass():
    g1 = LawnGrass("Trava", "Good lawn", 100.0, 50, "Россия", "7 дней", "Зеленый")
    g2 = LawnGrass("Trava2", "Better lawn", 120.0, 30, "США", "5 дней", "Светло-зеленый")
    assert g1 + g2 == 100.0 * 50 + 120.0 * 30

def test_add_mixed_types():
    sp = Smartphone("iPhone", "Best phone", 100000.0, 10, 98.5, "Pro", 512, "Черный")
    lg = LawnGrass("Trava", "Good lawn", 100.0, 50, "Россия", "7 дней", "Зеленый")
    with pytest.raises(TypeError):
        _ = sp + lg

def test_category_add_product():
    sp = Smartphone("iPhone", "Best phone", 100000.0, 10, 98.5, "Pro", 512, "Черный")
    cat = Category("Электроника", "Описание", [])
    cat.add_product(sp)
    assert len(cat.products.split("\n")) == 2
    assert Category.product_count == 1

    with pytest.raises(TypeError):
        cat.add_product("Не продукт")

def test_category_middle_price():
    product1 = Product("Product A", "Description A", 100.0, 5)
    product2 = Product("Product B", "Description B", 200.0, 10)
    product3 = Product("Product C", "Description C", 300.0, 15)

    category = Category("Test Category", "Description", [product1, product2, product3])
    assert category.middle_price() == 200.0  # (100 + 200 + 300) / 3

def test_category_middle_price_empty():
    category = Category("Empty Category", "No products", [])
    assert category.middle_price() == 0
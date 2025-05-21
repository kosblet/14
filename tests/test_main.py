import pytest
from ecommerce.main import Product, Smartphone, LawnGrass, Category

# Тесты для Product
def test_product_creation_with_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test", "Desc", 100.0, 0)

def test_product_price_setter_negative():
    product = Product("Test", "Desc", 100.0, 5)
    with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
        product.price = -50.0

def test_product_add_valid():
    p1 = Product("P1", "Desc1", 10.0, 2)
    p2 = Product("P2", "Desc2", 20.0, 3)
    assert p1 + p2 == 10*2 + 20*3

def test_product_add_invalid():
    p1 = Product("P1", "Desc1", 10.0, 2)
    s1 = Smartphone("S1", "Desc", 100.0, 1, 95.0, "Model", 128, "Black")
    with pytest.raises(TypeError, match="Нельзя складывать разные типы продуктов"):
        p1 + s1

def test_product_str():
    product = Product("Test", "Desc", 100.0, 5)
    assert str(product) == "Test, 100.0 руб. Остаток: 5 шт."

# Тесты для Smartphone
def test_smartphone_inheritance():
    s = Smartphone("iPhone", "Desc", 1000.0, 1, 95.0, "Pro", 256, "Silver")
    assert isinstance(s, Product)
    assert s.model == "Pro"

def test_smartphone_add():
    s1 = Smartphone("S1", "Desc", 100.0, 2, 95.0, "Model", 128, "Black")
    s2 = Smartphone("S2", "Desc", 200.0, 3, 95.0, "Model", 256, "White")
    assert s1 + s2 == 100*2 + 200*3

# Тесты для LawnGrass
def test_lawn_grass_inheritance():
    g = LawnGrass("Grass", "Desc", 50.0, 10, "USA", "30 days", "Green")
    assert isinstance(g, Product)
    assert g.country == "USA"

# Тесты для Category
def test_category_middle_price():
    p1 = Product("P1", "Desc1", 100.0, 2)
    p2 = Product("P2", "Desc2", 200.0, 3)
    category = Category("Test", "Desc", [p1, p2])
    assert category.middle_price() == (100 + 200) / 2

def test_category_middle_price_empty():
    category = Category("Empty", "Desc", [])
    assert category.middle_price() == 0

def test_category_add_product():
    category = Category("Test", "Desc", [])
    p = Product("P1", "Desc1", 100.0, 5)
    category.add_product(p)
    assert category.product_count == 1
    with pytest.raises(TypeError):
        category.add_product("Not a Product")

# Тесты для display_info
def test_product_display_info(capsys):
    p = Product("Test", "Desc", 100.0, 5)
    p.display_info()
    captured = capsys.readouterr()
    assert "Product: Test, Price: $100.0, Quantity: 5" in captured.out

def test_smartphone_display_info(capsys):
    s = Smartphone("iPhone", "Desc", 1000.0, 1, 95.0, "Pro", 256, "Silver")
    s.display_info()
    captured = capsys.readouterr()
    assert "Smartphone: iPhone, Model: Pro" in captured.out

import pytest
from ecommerce.main import Product, Category, Smartphone, LawnGrass


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


def test_category_counters():
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("P1", "Desc1", 100.0, 10)
    product2 = Product("P2", "Desc2", 200.0, 5)
    product3 = Product("P3", "Desc3", 300.0, 15)

    category1 = Category("Электроника", "Описание", [product1, product2])
    category2 = Category("Другое", "Ещё описание", [product3])

    assert Category.category_count == 2
    assert Category.product_count == 3
# tests/test_main.py

import pytest
from ecommerce.main import Product, Smartphone, LawnGrass, Category


def test_smartphone_inheritance():
    sp = Smartphone("iPhone", "Best phone", 100000.0, 10, 98.5, "Pro", 512, "Черный")
    assert isinstance(sp, Product)


def test_lawn_grass_inheritance():
    lg = LawnGrass("Trava", "Good lawn", 100.0, 50, "Россия", "7 дней", "Зеленый")
    assert isinstance(lg, Product)


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
    cat = Category("Смартфоны", "Телефоны", [])
    cat.add_product(sp)
    assert len(cat.products) > 0


def test_category_reject_invalid_type():
    cat = Category("Смартфоны", "Телефоны", [])
    with pytest.raises(TypeError):
        cat.add_product("Not a product")

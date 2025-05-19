from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех продуктов.
    """
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def display_info(self):
        """Метод для отображения информации о продукте."""
        pass


class LoggingMixin:
    """
    Миксин для логирования создания объекта.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Created object of class {self.__class__.__name__} with parameters: {args}, {kwargs}")


class Product(BaseProduct, LoggingMixin):
    """
    Конкретный класс продукта, наследуется от BaseProduct и LoggingMixin.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name, description, price, quantity)

    def display_info(self):
        print(f"Product: {self.name}, Description: {self.description}, Price: ${self.price}, Quantity: {self.quantity}")


class Smartphone(Product):
    """
    Класс для смартфонов, наследуется от Product.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int, screen_size: float, ram: int):
        super().__init__(name, description, price, quantity)
        self.screen_size = screen_size
        self.ram = ram

    def display_info(self):
        print(
            f"Smartphone: {self.name}, Screen Size: {self.screen_size} inches, RAM: {self.ram}GB, "
            f"Price: ${self.price}, Quantity: {self.quantity}"
        )


class LawnGrass(Product):
    """
    Класс для газонной травы, наследуется от Product.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int, color: str, country_of_origin: str):
        super().__init__(name, description, price, quantity)
        self.color = color
        self.country_of_origin = country_of_origin

    def display_info(self):
        print(
            f"Lawn Grass: {self.name}, Color: {self.color}, Country of Origin: {self.country_of_origin}, "
            f"Price: ${self.price}, Quantity: {self.quantity}"
        )


class Category:
    """
    Класс для категорий товаров.
    """
    category_count = 0  # Счетчик категорий
    product_count = 0   # Счетчик продуктов

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += sum(product.quantity for product in products)

    def middle_price(self):
        """
        Вычисляет среднюю цену товаров в категории.
        Если категория пустая, возвращает 0.
        """
        try:
            total_price = sum(product.price for product in self.products)
            return total_price / len(self.products) if self.products else 0
        except ZeroDivisionError:
            return 0

    def __repr__(self):
        return f"Category(name={self.name}, description={self.description}, products={len(self.products)})"


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(f"Возникла ошибка: {e}")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    print(f"Средняя цена в категории '{category1.name}': {category1.middle_price()}")

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(f"Средняя цена в категории '{category_empty.name}': {category_empty.middle_price()}")
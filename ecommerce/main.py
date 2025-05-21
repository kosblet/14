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

    def __add__(self, other):
        if type(self) is not type(other):  # Исправленная проверка
            raise TypeError("Нельзя складывать разные типы продуктов")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = value


class Smartphone(Product):
    """
    Класс для смартфонов, наследуется от Product.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Класс для газонной травы, наследуется от Product.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """
    Класс для категорий товаров.
    """
    category_count = 0  # Счетчик категорий
    product_count = 0   # Счетчик продуктов

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products or []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только экземпляры класса Product")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += f"{product}\n"
        return result

    def middle_price(self):
        """
        Вычисляет среднюю цену товаров в категории.
        Если категория пустая, возвращает 0.
        """
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products) if self.__products else 0
        except ZeroDivisionError:
            return 0

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


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

    try:
        print(product1 + product2)  # 180000*5 + 210000*8 = 2580000.0
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        product1.price = -100
    except ValueError as e:
        print(f"Ошибка: {e}")
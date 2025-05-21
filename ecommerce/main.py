from abc import ABC, abstractmethod

class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def display_info(self):
        pass


class LoggingMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Created {self.__class__.__name__}: {args}, {kwargs}")


class Product(BaseProduct, LoggingMixin):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name, description, price, quantity)
        self._price = price

    def display_info(self):
        print(f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def __add__(self, other):
        if type(self) is not type(other):
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
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def display_info(self):
        print(f"Smartphone: {self.name}, Model: {self.model}, Price: ${self.price}")


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def display_info(self):
        print(f"LawnGrass: {self.name}, Country: {self.country}, Price: ${self.price}")


class Category:
    category_count = 0  # Глобальный счетчик категорий

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products or []
        self.product_count = len(self.__products)  # Локальный счетчик продуктов
        Category.category_count += 1

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только экземпляры Product")
        self.__products.append(product)
        self.product_count += 1  # Увеличиваем локальный счетчик

    @property
    def products(self):
        return "\n".join(str(product) for product in self.__products)

    def middle_price(self):
        if not self.__products:
            return 0
        total = sum(p.price for p in self.__products)
        return total / len(self.__products)

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

if __name__ == '__main__':
    # Создание товаров
    try:
        invalid_product = Product("Invalid", "Invalid product", 1000.0, 0)
    except ValueError as e:
        print(f"Ошибка: {e}")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создание категории
    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    print(f"Средняя цена в категории '{category1.name}': {category1.middle_price()}")

    # Пустая категория
    empty_category = Category("Пустая категория", "Категория без продуктов", [])
    print(f"Средняя цена в категории '{empty_category.name}': {empty_category.middle_price()}")

    # Тест сложения продуктов
    try:
        total_price = product1 + product2
        print(f"Общая стоимость товаров: {total_price}")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Тест сеттера цены
    try:
        product1.price = -100
    except ValueError as e:
        print(f"Ошибка: {e}")
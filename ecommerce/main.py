# src/main.py

from collections import Counter


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self.__price = value

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list = None):
        """
        Создаёт или обновляет существующий продукт.
        Если продукт с таким именем уже есть — обновляет количество и цену.
        """
        if existing_products is None:
            existing_products = []

        for product in existing_products:
            if product.name == product_data["name"]:
                product.quantity += product_data.get("quantity", 0)
                product.price = max(product.price, product_data.get("price", product.price))
                return product

        return cls(**product_data)

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать разные типы продуктов")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Category:
    category_count = 0
    product_count = 0

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
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category("Смартфоны", "Смартфоны как средство коммуникации", [product1, product2, product3])
    print(str(category1))

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(str(category1))

    print(category1.products)

    # Попытка сложения
    print(product1 + product2)  # 180000*5 + 210000*8 = 2580000.0
    try:
        print(product1 + product4)  # ❌ TypeError
    except TypeError as e:
        print(f"Ошибка: {e}")

    # new_product
    new_product = Product.new_product({
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }, [product1, product2, product3])

    print(new_product.quantity)  # 5 + 5 = 10
    print(new_product.price)    # 180000.0

    try:
        product1.price = -100
    except ValueError as e:
        print(f"Ошибка: {e}")
    product1.price = 190000.0
    print(product1.price)  # 190000.0
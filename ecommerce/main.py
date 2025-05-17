
class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать разные типы продуктов")
        return (self.price * self.quantity) + (other.price * other.quantity)

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
            result += f"{product}\n"
        return result

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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

    try:
        print(product1 + product2)  # 180000*5 + 210000*8 = 2580000.0
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        product1.price = -100
    except ValueError as e:
        print(f"Ошибка: {e}")
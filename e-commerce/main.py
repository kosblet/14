class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация продукта.
        :param name: Название продукта (str).
        :param description: Описание продукта (str).
        :param price: Цена продукта (float).
        :param quantity: Количество продукта в наличии (int).
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    # Атрибуты класса для подсчета количества категорий и товаров
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """
        Инициализация категории.
        :param name: Название категории (str).
        :param description: Описание категории (str).
        :param products: Список объектов класса Product.
        """
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счетчики при создании новой категории
        Category.category_count += 1
        Category.product_count += len(products)
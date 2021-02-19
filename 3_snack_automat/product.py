"""Module required to manage products
"""


class Product:
    """Represents a single product
    """

    def __init__(self, name: str, price: int, amount: int):
        self.name = name
        self.price = price
        self.amount = amount

    def reduce(self, amount: int):
        """Reduces the product amount by the given number

        Args:
            amount (int): Quantity to reduce

        Raises:
            Exception: Thrown if product is out of stock
        """
        if self.amount < amount:
            raise ProductNotAvailibleException(
                f'Product is out of stock. Current quantity: {self.amount} ')
        self.amount -= amount


class ProductNotAvailibleException(Exception):
    """Raised when product is not availible
    """

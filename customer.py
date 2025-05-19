from order import Order

class Customer:
    def __init__(self, name):
        self.name = name  
        self._all_orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def _add_order(self, order):
        self._all_orders.append(order)

    def orders(self):
        return self._all_orders

    def coffees(self):
        return list(set(order.coffee for order in self._all_orders))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from coffee import Coffee  
        customer_totals = {}
        for order in coffee.orders():
            customer = order.customer
            customer_totals[customer] = customer_totals.get(customer, 0) + order.price

        if not customer_totals:
            return None

        return max(customer_totals, key=customer_totals.get)
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from coffee import Coffee
from customer import Customer

def test_coffee_name_and_immutability():
    coffee = Coffee("Mocha")
    assert coffee.name == "Mocha"

    with pytest.raises(AttributeError):
        coffee.name = "NewName"  # name should be immutable

def test_coffee_orders_and_customers():
    coffee = Coffee("Americano")
    customer1 = Customer("Sam")
    customer2 = Customer("Jane")

    order1 = customer1.create_order(coffee, 3.5)
    order2 = customer2.create_order(coffee, 4.0)

    orders = coffee.orders()
    customers = coffee.customers()

    assert order1 in orders and order2 in orders
    assert customer1 in customers and customer2 in customers

def test_num_orders_and_average_price():
    coffee = Coffee("Cappuccino")
    customer = Customer("Alex")

    assert coffee.num_orders() == 0
    assert coffee.average_price() == 0

    customer.create_order(coffee, 5.0)
    customer.create_order(coffee, 7.0)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 6.0
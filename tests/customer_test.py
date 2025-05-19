import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_property():
    c = Customer("Alice")
    assert c.name == "Alice"

    # test setter enforces type and length
    with pytest.raises(TypeError):
        c.name = 123  # not a string

    with pytest.raises(ValueError):
        c.name = ""  # too short

    with pytest.raises(ValueError):
        c.name = "A"*20  # too long

def test_customer_orders_and_coffees():
    customer = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")

    order1 = customer.create_order(coffee1, 5.0)
    order2 = customer.create_order(coffee2, 4.5)
    order3 = customer.create_order(coffee1, 6.0)

    # orders() returns all orders
    orders = customer.orders()
    assert order1 in orders and order2 in orders and order3 in orders

    # coffees() returns unique coffee instances
    coffees = customer.coffees()
    assert coffee1 in coffees and coffee2 in coffees
    assert len(coffees) == 2
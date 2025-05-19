import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_properties():
    customer = Customer("Linda")
    coffee = Coffee("Flat White")
    order = Order(customer, coffee, 4.5)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.5

    with pytest.raises(AttributeError):
        order.price = 5.0  # price should be immutable

def test_invalid_order_initialization():
    customer = Customer("Linda")
    coffee = Coffee("Flat White")

    with pytest.raises(TypeError):
        Order("not_a_customer", coffee, 5.0)

    with pytest.raises(TypeError):
        Order(customer, "not_a_coffee", 5.0)

    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  # price too low

    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0)  # price too high
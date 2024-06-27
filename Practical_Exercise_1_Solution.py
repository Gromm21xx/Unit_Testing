import pytest
from your_main_file import Customer

def test_get_membership_level():
    customer1 = Customer("test1@example.com", 1000, 1)
    customer2 = Customer("test2@example.com", 2000, 3)
    customer3 = Customer("test3@example.com", 3000, 6)

    assert customer1.get_membership_level() == "Bronze"
    assert customer2.get_membership_level() == "Silver"
    assert customer3.get_membership_level() == "Gold"

def test_get_customer_info():
    customer = Customer("test@example.com", 1500, 2)
    expected_info = "Email: test@example.com, Total Spent: £1500, Membership Level: Silver"
    assert customer.get_customer_info() == expected_info

def test_customer_attributes():
    customer = Customer("test@example.com", 1000, 1)
    assert customer.email == "test@example.com"
    assert customer.total_spent == 1000
    assert customer.membership_length == 1

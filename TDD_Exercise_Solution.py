# In test_customer.py

import pytest
from your_main_file import Customer  # Replace 'your_main_file' with the actual filename

# ... (previous test functions) ...

def test_get_discount():
    customer1 = Customer("test1@example.com", 500, 1)
    customer2 = Customer("test2@example.com", 1500, 3)
    customer3 = Customer("test3@example.com", 3000, 5)

    assert customer1.get_discount() == 0
    assert customer2.get_discount() == 5
    assert customer3.get_discount() == 10
    
    # Edge case
    customer4 = Customer("test4@example.com", 0, 1)
    assert customer4.get_discount() == 0

# In your main file (e.g., customer.py)

class Customer:
    # ... (previous methods) ...

    def get_discount(self):
        if self.total_spent >= 2000:
            return 10
        elif self.total_spent >= 1000:
            return 5
        else:
            return 0

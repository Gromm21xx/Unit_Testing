# In customer.py

import requests

class Customer:
    # ... (previous methods) ...

    def get_reward_points(self):
        try:
            response = requests.get("https://api.example.com/reward-rate")
            rate = response.json()["rate"]
            return int(self.total_spent * rate)
        except:
            return 0

# In test_customer.py

from unittest.mock import patch
import pytest
from customer import Customer

# ... (previous tests) ...

@patch('customer.requests.get')
def test_get_reward_points(mock_get):
    customer = Customer("test@example.com", 1000, 1)
    
    # Test successful API call
    mock_get.return_value.json.return_value = {"rate": 0.1}
    assert customer.get_reward_points() == 100

    # Test different rate
    mock_get.return_value.json.return_value = {"rate": 0.2}
    assert customer.get_reward_points() == 200

    # Test API failure
    mock_get.side_effect = Exception("API error")
    assert customer.get_reward_points() == 0

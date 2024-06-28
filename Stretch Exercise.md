# Unit Testing

## Stretch Exercise: Advanced Testing Techniques - Mocking and Patching

## Exercise instructions:

1.	New Feature: Customer Reward Points - We want to add a method that calculates reward points based on the customer's total spent, but it requires an external API call to get the current reward rate.
2.	Open your main file (e.g., customer.py) and add a placeholder for the new method
3.	Open your test_customer.py file. 
4.	 Import the necessary mocking tools - from unittest.mock import patch
5.	Write a new test method: 
    * Create a test function called test_get_reward_points()
    * Use the @patch decorator to mock the external API call
6.	Run the tests:
    * Use the command: pytest test_customer.py
    * Observe that the new test fails (Red phase)
7.	Implement the feature: 
    * In your main file, implement the get_reward_points() method
    * Use requests.get() to simulate an API call (we'll mock this in our tests)
8.	Update your test to mock the API call: 
    * Use mock_get.return_value to simulate the API response
    * Write assertions to check if the reward points are calculated correctly
9.	Run the tests again: 
    * Use the command: pytest test_customer.py
    * Ensure all tests now pass (Green phase)
10.	Add more test cases: 
    * Test different API responses
    * Test error handling (e.g., API failure)
11.	Final test run: 
    * Run pytest test_customer.py one last time
    * Ensure all tests, including the original ones, still pass
      
### **Remember:**
  * Mocking allows us to test our code in isolation from external dependencies
  * Use patching to replace functions or objects only within the scope of a test
  * Consider different scenarios, including error cases

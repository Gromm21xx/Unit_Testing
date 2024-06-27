# Unit Testing

## Practical Exercise 2: Test Driven Design

## Exercise instructions:

1. New Feature: Customer Discount We want to add a new method to calculate a customer's discount based on their total spent. 
2. Open your test_customer.py file. 
3. Write a new test method: 
    * Create a test function called test_get_discount()
    * This test should fail initially (Red phase)
4. Run the tests: 
    * Use the command: pytest test_customer.py
    * Observe that the new test fails
5. Implement the feature: 
    * Open your main file containing the Customer class
    * Add a new method called get_discount()
    * Write minimal code to make the test pass (Green phase)
6. Run the tests again: 
    * Use the command: pytest test_customer.py
    * Ensure all tests now pass
7. Refactor (if necessary): 
    * Improve the code without changing its behavior
    * Run tests after each change to ensure they still pass
8. Add more test cases: 
    * In test_customer.py, add more assertions to test_get_discount()
    * These should cover different spending amounts and edge cases
9. Run the tests and implement: 
    * Run tests, observe failures
    * Modify get_discount() to handle all cases
    * Repeat until all tests pass
10. Final test run: 
    * Run pytest test_customer.py one last time
    * Ensure all tests, including the original ones, still pass


### **Remember:**
   * Follow the Red-Green-Refactor cycle strictly
   * Write the simplest code possible to make tests pass
   * Only refactor when tests are green

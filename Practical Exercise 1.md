# Unit Testing

## Practical Exercise 1: Unit Testing with pytest

## Exercise instructions:



1. Create a new file: 
   * Open your code editor 
   * Create a new file named test_customer.py in the same directory as your main code file 
2. Import required modules and class: 
   * At the top of test_customer.py, import pytest and the Customer class from your main file 
   * Write test functions: 
     Create three test functions in test_customer.py:
         *  a) test_get_membership_level()
         * b) test_get_customer_info()
         * c) test_customer_attributes() 
         * Test the get_membership_level method: 
         * In test_get_membership_level(), create three Customer objects with different membership lengths 
         * Use assert statements to check if each customer's membership level is correct 
4. Test the get_customer_info method: 
         * In test_get_customer_info(), create a Customer object 
         * Define the expected info string 
         * Use an assert statement to check if the method's output matches the expected string 
5. Test the Customer attributes: 
         * In test_customer_attributes(), create a Customer object 
         * Use assert statements to check if the object's attributes match the values you provided 
6. Save the file: 
         * Make sure to save test_customer.py after adding all the test functions 
7. Run the tests: 
         * Open your terminal or command prompt 
         * Navigate to the directory containing your Python files 
         * Run the command: pytest test_customer.py 
8. Observe the results: 
         * pytest will run all the tests and display the results 
         * You should see output indicating whether each test passed or failed
   
**Remember:**
Use the AAA (Arrange-Act-Assert) pattern in your tests 
Consider different scenarios, including edge cases 
Use meaningful test function names that describe what's being tested

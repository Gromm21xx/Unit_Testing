
# Unit Testing

## Practical Exercise 1: Writing Unit Tests using the unittest Class

## Exercise instructions:


1. Create a new file called calculator.py in your project directory and add the following code:
   
        def add(a, b):
           return a + b

        def subtract(a, b):
           return a - b

2. Create another new file called test_calculator_unittest.py in the same directory.
3. Open test_calculator_unittest.py and add the following import statements at the top:

        import unittest
        from calculator import add, subtract

4. Create a class called TestCalculator that inherits from unittest.TestCase:

        class TestCalculator(unittest.TestCase):

5. Inside the TestCalculator class, create two test methods:
        
        test_add: Test the add function
        test_subtract: Test the subtract function

7. In test_add, use self.assertEqual to test the add function with different inputs.
8. In test_subtract, use self.assertEqual to test the subtract function with different inputs.
9. After the class definition, add the following code to run the tests:
        
        if __name__ == '__main__':
            unittest.main()

10. Save the file.
11. Run the tests from the command line using:

        -m unittest test_calculator_unittest.py

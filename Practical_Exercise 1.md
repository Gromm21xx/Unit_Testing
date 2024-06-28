
# Unit Testing

## Practical Exercise 1: Writing Unit Tests using the unittest Class

## Exercise instructions:


1. Create a new file called test_calculator_unittest.py in your project directory.
2. Open test_calculator_unittest.py and add the following import statements at the top:

    import unittest
    from calculator import add, subtract

3. Create a class called TestCalculator that inherits from unittest.TestCase:
        
    class TestCalculator(unittest.TestCase):

4. Inside the TestCalculator class, create two test methods:
        
    test_add: Test the add function
    test_subtract: Test the subtract function

5. In test_add, use self.assertEqual to test the add function with different inputs.
6. In test_subtract, use self.assertEqual to test the subtract function with different inputs.
7. After the class definition, add the following code to run the tests:
        
    if __name__ == '__main__':
        unittest.main()

8. Save the file.
9. Run the tests from the command line using:

    -m unittest test_calculator_unittest.py
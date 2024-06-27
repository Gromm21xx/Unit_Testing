# Modules, Packages & Virtual Environments

## Practical Exercise 1: Creating Modules

## Exercise instructions:


1. Create a new directory called customer_management on your desktop. 
2. Inside the customer_management directory, create a new file called customer.py. 
3. Copy and paste the Customer class code from the previous session into customer.py. 
4. Create another file in the customer_management directory called customer_utils.py. 
5. In customer_utils.py, define two new utility functions: 
    * get_preferred_customers(customers): This function should take a list of customer instances and return a list of preferred customers based on the criteria of total spent > 1000 or membership length > 2. 
    * get_customer_emails(customers): This function should take a list of customer instances and return a list of their email addresses. 
6. Create a new file in the customer_management directory called main.py. 
7. In main.py, import the necessary classes and functions: 
    * Import the pandas library. 
    * Import the Customer class from the customer module. 
    * Import the get_preferred_customers and get_customer_emails functions from the customer_utils module. 
8.  Load the "Ecommerce Customers.csv" dataset using pandas, just like in the previous session. 
9.  Create instances of the Customer class based on the dataset, similar to the previous session. 
10. Use the newly created utility functions get_preferred_customers and get_customer_emails to perform operations on the customer instances. 
11. Print the preferred customers' information and the list of customer emails. 
12. Run the main.py script and observe the output. 
    
**Stretch Activity:**

1. Open the customer_utils.py file. 
2. Add a new utility function called get_top_spenders(customers, n) that takes a list of customer instances and an integer n as parameters. This function should return the top n customers based on their total amount spent. 
3. Open the main.py file and import the get_top_spenders function from the customer_utils module. 
4. Call the get_top_spenders function with the list of customers and a desired value of n, and print the information of the top spenders.

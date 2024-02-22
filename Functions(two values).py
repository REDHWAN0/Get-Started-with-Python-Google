# Refine the `total_sales` function
def total_sales(price, num_tickets):
    return round(price * num_tickets, 2)
# Call the function with two values
print(total_sales(15.99, 1001))

# Call `total_sales` with 16.99 price and 1232 num_tickets
print(total_sales(16.99, 1232))

# Call `total_sales` with 10.50 price and 1472 num_tickets
print(total_sales(10.50, 1472))

# Call `total_sales` with 5.00 price and 349 num_tickets
print(total_sales(5.00, 349))
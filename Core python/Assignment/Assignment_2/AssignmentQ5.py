# WAP to calculate selling price of book based on cost price and discount.

cost_price = int(input("Enter the cost price of the book: "))
discount = int(input("Enter the discount percentage: "))

discount_amount = (cost_price * discount) / 100

# Calculate selling price
selling_price = cost_price - discount_amount

print("Selling Price of the book =", selling_price)
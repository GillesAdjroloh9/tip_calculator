# Prompt food price from user 
food_price = float(input("Kindly enter your meal's price: $"))

# Calculate the sales tax (7%)
tip = 0.8 * food_price

# Calculate the sales tax (7&)
sales_tax = 0.07 * food_price

# Calculate the Grand total of the meal
total_cost = food_price + tip + sales_tax

# Display the calculated amounts
print(f"Tip(18%) = ${tip:.2f}")
print(f"Sales Tax(7%) = ${sales_tax:.2f}")

# Display the total cost 
print(f"Grand Total = ${total_cost:.2f}")

# Question 2: Shipping Tax Calculator

# Get the price and the shipping state from the user
price = float(input("Enter the price of the sale item (e.g., 3.99): "))
state = input("Enter the state to which the item to be shipped (e.g., TX, LA, CA): ").upper().strip()

# Check conditions to assign the correct shipping tax
if state == "TX" or state == "LA":
    shipping_tax = 1.25
elif state == "CA":
    shipping_tax = 3.25
else:
    shipping_tax = 0.50

# Display the shipping tax
print("The shipping tax for", state, "is:", shipping_tax)

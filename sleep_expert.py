# Question 1: Sleep Expert Program

# Get input from the user and convert it to a float to handle decimal ounces
ounces = float(input("How many oz of milk the child drank? "))

# Determine sleep outcome based on the amount of milk
if ounces >= 6:
    print("Baby will sleep well for 5 hours")
else:
    print("Baby will not sleep well. So be prepared")

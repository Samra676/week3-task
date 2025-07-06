# Step 1: Input from user
products = int(input("Enter number of products: "))
total_price = float(input("Enter total price: "))

# Step 2: Apply discount
if total_price > 1000 and products > 3:
    discount = 0.15 * total_price
elif total_price > 500:
    discount = 0.10 * total_price
else:
    discount = 0.0

# Step 3: Calculate final amount
final_bill = total_price - discount

# Step 4: Show result
print(f"\nTotal Price: Rs. {total_price:.2f}")
print(f"Discount Applied: Rs. {discount:.2f}")
print(f"Final Bill to Pay: Rs. {final_bill:.2f}")

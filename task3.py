#Ask user for monthly income and expenses.
#Calculate savings and classify:
#>10000 = Saving Well, 5000-9999 = Average, <5000 = Try to Save.



# Step 1: Input from user
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))

# Step 2: Calculate savings
savings = income - expenses

# Step 3: Classify savings
if savings > 10000:
    status = "Saving Well"
elif 5000 <= savings <= 9999:
    status = "Average"
else:
    status = "Try to Save"

# Step 4: Display results
print(f"\nYour savings: {savings:.2f}")
print(f"Status: {status}")

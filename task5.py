#Ask user for attendance (%) and final marks. If attendance ≥ 75 and marks ≥ 50 'n Promote Else 'n Not promoted.
# Step 1: Get input from user
attendance = float(input("Enter your attendance percentage: "))
marks = float(input("Enter your final marks: "))

# Step 2: Check both conditions
if attendance >= 75 and marks >= 50:
    print(" Promoted")
else:
    print(" Not Promoted")

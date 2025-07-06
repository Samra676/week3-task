#Take marks of 3 subjects.
#Calculate total, percentage and assign grade:
#A (>=85), B (>=70), C (>=50), Fail (<50).
# Step 1: Take input of marks for 3 subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

# Step 2: Calculate total and percentage
total_marks = sub1 + sub2 + sub3
percentage = (total_marks / 300) * 100  # Assuming each subject is out of 100

# Step 3: Assign grade based on percentage
if percentage >= 85:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

# Step 4: Display result
print(f"\nTotal Marks: {total_marks}/300")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")

#Build a login system. Ask username & password.
#If username = 'admin' and password = '1234', print Access Granted. Else, Access Denied.
# Step 1: Ask for username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Step 2: Check credentials
if username == "admin" and password == "1234":
    print("Access Granted ")
else:
    print("Access Denied ")

Name = input("Enter your username: ")
Pass = input("Enter your password: ")
if Name == "admin":
    if Pass == "1234":
        print("Access granted")
    else:
        print("Access denied")
else:
    print("Access denied")

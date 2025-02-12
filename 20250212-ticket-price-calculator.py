age = input("Your age is: ")
if int(age) > 65: 
    print("The ticket price is 17$")
elif int(age) >25:
    print("The ticket price is 20$")
elif int(age) >18:
    print("The ticket price is 12$")
else:
    print("The ticket price is free")

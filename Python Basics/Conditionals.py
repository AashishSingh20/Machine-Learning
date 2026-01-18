'''
# if condition 
a = 4
if(a > 3):
    print(f"{a} is greater than 3")
'''

'''
# if-else condition
a = 5
b = 10
if(b < a):
    print("b is smaller")
else:
    print("b is greater")
'''

'''
# if - elif - else
a = 10
if(a > 100):
    print("a is greater than 100")
elif a < 100:
    print("a is lesser than 100")
else:
    print("a is equal to 100")
'''

'''
# Nested if-else
x = 10
y = 5

if(x > y):
    if(y > 5):
        print("Both x and y is greater than 5 ")
    else:
        print("x is greater than 5 but y is not ")
else:
    print("x is not greater than 5")
'''

name = input("Enter your Name: ")
email = input("Enter your Email: ")
password = input("Enter your Password: ")

if (name == ""):
    print("Name cannot be empty.")
else:
    if("@" not in email):
        print("Invalid Email Address.")
    else:
        if(len(password) < 8):
            print("Enter Password of atleast length 8.")
        else:
            print("Registration Successfull.")
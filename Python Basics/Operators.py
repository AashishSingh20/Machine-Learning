'''
# Arithematic Operators(1)
# Add
a = 5
b = 2
print(a+b)

# Subtract
print(a-b)

# Multiply
print(a*b)

# Division
print(a/b)

# Floor Operator
print(a // b)  # Just like Division,but gives nearest previous integer not decimal

# Modulus 
print(a%b)

# power
print(a**b)
'''

'''
# Comparison Operators(2)
# Equal To
print(2 == 2)  # gives True
print(2 == 3)  # gives False

# Not Equal To
print(2 != 3)
print(2 != 2)

# Greater Than
print(2 > 1)
print(4 > 5)

# Less Than
print(4 < 5)
print(2 < 1)

# Greater than Equal To
print(5 >= 5)
print(6 >= 7)

# Less than Equal To 
print(5 <= 6)
print(4 <= 3)
'''

'''
# Logical Operators(3)
# AND                # T&T = T , T&F = F , F&T = F , F&F = F
print(True & True)   
print(True & False)

# OR                 # T|T = T , T|F = T , F|T = T , F|F = F
print(True | False) 
print(False | False)

# NOT                # not T = F , not F = T
print(not False) 
print(not True)
'''

'''
# Assignment Operators
a = 10
print(a)

a = a+5
print(a)

a += 5
print(a)

a *= 2
print(a)

a /= 2
print(a)
'''

'''
# MemberShip Operators
# in
a = "Aashish"
print("A" in a)  # Agar 'A' is in a then it gives TRUE or FALSE
print("ash" in a)  # Can be used for multiple characters in string as well

b = ["data", "science", "ajay"]
print("data" in b)

#not in
print("A" not in a)
print("qs" not in a)
'''

'''
# Identity Operators    # Compares Memory Location of Two Objects
a = 2
b = 3

print(a is b)  # Kya a and b same address par point kar rahe hai? - NO, so False
print(a is not b)  # Kya a and are both pointing to different memory location? - YES, so True

X = 4
Y = X
print(X is Y)  # Kya X and Y both pointing to same memory Location - YES, so True
print(X is not Y)  # Gives False
'''

# Bitwise Operator
print(10 & 10)
print(bin(10))  # This gets us the Binary Representation of 10 
print(18 & 3) 

print(18 | 6)  
print(~7)

#XOR    #Returns 1 when exactly one operand is 1
print(5^3) 

# Shift Operator
# Left Shift
print(8 << 2)   # Left shift binary numbers of 8 by 2 position 

# Right Shift
print(9 >> 3)  # Right shift binary numbers of 9 by 3 position
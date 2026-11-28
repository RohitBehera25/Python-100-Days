# ! Operators In Python

# 1. Arithmetic Operators.
# 2. Comparsion Operators.
# 3. Logical Operators.
# 4. Bitwise Operators.
# 5. Assignment Operators.
# 6. Identity Operators.
# 7. Membership Operators.

#? 3. Logical Operators.

x = True
y = False

print(x or y)

U = False
V = True

print(U and V)

print(not V)

# ? Bitwise Operators.

x = 2
y = 3

print(x & y)  # 2
print(x | y)  # 3
print(x >> 2) # 0
print(y << 3) # 24
print(~x)     # -3

# ? Identity Operators.

a = 3
b = 3

print(a is b) # True

a = "Hello"
b = "Hello"

print(a is b) # True

c = [1,2,3]
d = [1,2,3]

print(c is d) # False

e = "Hello-world"
f = "Hello-world"

print(e is f) # True

# ? Membership Operators

x  = "Delhi"

print("D" in x) #True
print("l" in x) #True
print("h" not in x) #False
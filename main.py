import math
# String
my_name = "mujahidul islam Munna"
print(len(my_name))
print(my_name[0])
print(my_name[-1])
print(my_name[0:7])
print(my_name[0:])
print(my_name[0:7])
print(my_name[:])
# String Method
print(my_name.upper())
print(my_name.lower())
print(my_name.title())
print(my_name.strip())
print(my_name.find("Mun"))
print(my_name.replace("m", "j"))
print("Mun" in my_name)
print("mun" not in my_name)
# Number
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10 % 3)
print(10**3)

x = 10
x = x + 3
x += 3

# Working with numbers
print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.2))

# Type Conversion
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

# int(x)
# float(x)
# bool(x)
# str(x)

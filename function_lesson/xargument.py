# *argument

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 5))

# **argument


def save_user(**user):
    print(user["name"])


save_user(id=1, name="john", age=20)

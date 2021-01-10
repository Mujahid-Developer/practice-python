# Type of function
# 1- Perform a task
# 2- Return a value

def get_greeting(name):
    return f"Hi {name}"


massage = get_greeting("Mujahid")

file = open("content.txt", "w")
file.write(massage)

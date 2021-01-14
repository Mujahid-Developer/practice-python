# local Variable
def greet(name):
    massage = "Hello"
    print(massage + " " + name)


greet("Mujahid")

# Global Variables
username = "Mujahid"


def greeting(lastname):
    print(username + " " + lastname)
    return greeting


greeting("Islam")

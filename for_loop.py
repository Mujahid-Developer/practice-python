for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# for else
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("You are successfully used 'For else'")
        break
else:
    print("Attempted 3 times Failed")

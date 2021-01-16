letters = ["a", "b", "c", "d"]

# adding
letters.append("f")
letters.insert(1, "_")
print(letters)
# remove
letters.pop()
letters.pop(1)
letters.remove("b")
del letters[0:2]
letters.clear()
print(letters)

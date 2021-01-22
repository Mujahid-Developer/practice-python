items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]
# Mapping (List comprehension)
x = [item[1] for item in items]
print(x)

# Filtered (List comprehension)
filtered = [item[1] for item in items if item[1] >= 10]
print(filtered)

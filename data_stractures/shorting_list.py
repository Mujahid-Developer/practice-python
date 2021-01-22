numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))
print(numbers)
# Examples:
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),

]


def sort_items(item):
    return item[1]


items.sort(key=sort_items)
print(items)

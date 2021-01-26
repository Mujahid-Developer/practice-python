from sys import getsizeof

values = (x*2 for x in range(100000))
# print(values)
# for x in values:
#     print(x)
print("Gen:", getsizeof(values))

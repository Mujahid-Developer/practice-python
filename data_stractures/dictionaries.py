point = {"x": 1, "y": 2}
# list()
# tuple()
# set()
# dict()
point = dict(x=1, y=2)
point["x"] = 10
point["y"] = 20
# print(point)
# for key in point:
#     print(key, point[key])
for key, value in point.items():
    print(key, value)

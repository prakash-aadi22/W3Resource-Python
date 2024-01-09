color = ['Red', 'Blue', 'Black', 'White', 'Pink']
# print(list(map(list, color)))
print(list(map(lambda x: list(x), color)))

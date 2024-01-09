def add(d, value, key):
    d.update({value: key})
    print(d)


add({0: 10, 1: 20}, 4, 40)

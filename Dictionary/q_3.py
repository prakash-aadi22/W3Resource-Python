def add(d1, d2, d3):
    d4 = {}
    for d in (d1, d2, d3):
        d4.update(d)
    print(d4)


# def update_method(d1, d2, d3):
def update_method():
    concatenated_dict = dic1.copy()
    concatenated_dict.update(dic2)
    concatenated_dict.update(dic3)
    print("Concatenated dictionary using update(): ", concatenated_dict)


def unpacking_method(d1, d2, d3):
    print({**d1, **d2, **d3})


dic1 = {'a': 1, 'b': 2}
dic2 = {'c': 3, 'd': 4}
dic3 = {'e': 5, 'f': 6}

add(dic1, dic2, dic3)

# update_method(dic1, dic2, dic3)
update_method()

unpacking_method(dic1, dic2, dic3)

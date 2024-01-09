def loop():
    for k, v in d.items():
        print(k + ":", v)

    for k in d.keys():
        print(k)

    for v in d.values():
        print(v)


d = {'x': 10, 'y': 20, 'z': 30}
loop()

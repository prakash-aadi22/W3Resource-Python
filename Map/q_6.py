c = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print(set(map(lambda s: (str(s).upper(), str(s).lower()), c)))

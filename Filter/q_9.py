strings = ["Red", "Green", "Orange", "White", "Black", "Pink", "Yellow"]
print(list(filter(lambda s: s.find('l') != -1, strings)))
print(list(filter(lambda s: s.find('l') >= 0, strings)))
print(list(filter(lambda s: s.find('l') > 0, strings)))
print(list(filter(lambda s: 'l' in s, strings)))

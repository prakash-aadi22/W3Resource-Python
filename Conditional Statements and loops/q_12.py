def change(lst):
    for i in lst:
        return i.upper()


def change1(lst1):
    for i in lst1:
        print(i.upper())


def change2(lst2):
    return [i.upper() for i in lst2]


a = []
lines = []
while True:
    x = input()
    if x:
        a.append(x)
        lines.append(x.upper())
    else:
        break
for st in lines:
    print(st)
print("---------------")
print(change(a))
print("---------------")
change1(a)
print("---------------")
print(change2(a))

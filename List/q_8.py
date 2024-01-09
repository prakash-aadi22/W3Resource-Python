def check(lst):
    if not lst:
        print("List is empty.")
    else:
        print("List is not empty.")


def check1(lst):
    if lst:
        print("List is not empty.")
    else:
        print("List is empty.")


def check2(lst):
    if not bool(lst):
        print("List is empty.")
    else:
        print("List is not empty.")


def check3(lst):
    if bool(lst):
        print("List is not empty.")
    else:
        print("List is empty.")


check([])
check([1, 2, 3])

check1([])
check1([1, 2, 3])

check2([])
check2([1, 2, 3])

check3([])
check3([1, 2, 3])

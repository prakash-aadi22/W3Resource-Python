def check(dic):
    if not dic:
        print("Dictionary is empty.")
    else:
        print("Dictionary is not empty.")


def check1(dic):
    if dic:
        print("Dictionary is not empty.")
    else:
        print("Dictionary is empty.")


def check2(dic):
    if not bool(dic):
        print("Dictionary is empty.")
    else:
        print("Dictionary is not empty.")


def check3(dic):
    if bool(dic):
        print("Dictionary is not empty.")
    else:
        print("Dictionary is empty.")


check({})
check({1: 10, 2: 20, 3: 30})

check1({})
check1({1: 10, 2: 20, 3: 30})

check2({})
check2({1: 10, 2: 20, 3: 30})

check3({})
check3({1: 10, 2: 20, 3: 30})

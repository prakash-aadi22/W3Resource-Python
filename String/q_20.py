def reverse_string(s):
    if len(s) % 4 == 0:
        print(s[::-1])
        print("".join(reversed(s)))


reverse_string("Python3.0")
reverse_string("Java")
reverse_string("HTML")
reverse_string("JavaScript")

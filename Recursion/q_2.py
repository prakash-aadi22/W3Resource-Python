def to_string(n, base):
    convert_to_string = "0123456789ABCDEF"
    if n < base:
        return convert_to_string[n]
    else:
        return to_string(n // base, base) + convert_to_string[n % base]


print(to_string(2835, 16))

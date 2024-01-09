mixed_case_strings = ["Hello", "w3resource", "Python", "Filter", "Learning"]
print(list(filter(lambda c: c.isupper(), "".join(mixed_case_strings))))

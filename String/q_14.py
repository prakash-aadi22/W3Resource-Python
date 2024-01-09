def sorted_list(s):
    print(", ".join(sorted(list(set([word for word in s.split(", ")])))))


sorted_list("red, white, black, red, green, black")
sorted_list("red, black, pink, green")

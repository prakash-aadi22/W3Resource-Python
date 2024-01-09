def check(s):
    # if s == "a" or s == "e" or s == "i" or s == "o" or s == "u":
    #     return True
    # else:
    #     return False
    all_vowels = "aeiou"
    return s in all_vowels


print(check(input("Letter: ")))

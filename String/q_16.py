def mid_insert(word, insert):
    if len(word) % 2 == 0:
        return word[:int(len(word) / 2)] + insert + word[int(len(word) / 2):]
    return "can't insert"


print(mid_insert("[[]]", "Python"))
print(mid_insert("{{}}", "PHP"))
print(mid_insert("<<>>", "HTML"))
print(mid_insert("(())", "JAVA"))
print(mid_insert("-> <-", "JAVA"))

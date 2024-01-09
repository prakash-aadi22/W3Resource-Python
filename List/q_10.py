def longer_word(n, lst):
    print([i for i in lst.split(" ") if len(i) > n])


def longer_words(n, lst):
    print([i for i in lst if len(i) > n])


longer_word(3, "The quick brown fox jumps over the lazy dog")
longer_words(3, ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"])

import string


def is_pangram(str1, alphabet=string.ascii_lowercase):
    alpha_set = set(alphabet)
    str_set = set(str1.lower())
    return alpha_set <= str_set


print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello"))

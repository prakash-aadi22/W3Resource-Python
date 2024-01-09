def reverse_string_words(s):
    return ' '.join(s.split(" ")[::-1])


def reverse_string_words1(s):
    words = s.split()
    punctuation = '.,?!;:'
    reversed_words = []
    for word in words:
        separated_word = word.rstrip(punctuation)
        punctuation_part = word[len(separated_word):]
        reversed_word = separated_word[::-1] + punctuation_part
        reversed_words.append(reversed_word)
    return ' '.join(reversed_words[::-1])


def reverse_string_words2(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
print(reverse_string_words("Python Exercises."))

print(reverse_string_words1("The quick brown fox jumps over the lazy dog."))
print(reverse_string_words1("Python Exercises."))

print(reverse_string_words2("The quick brown fox jumps over the lazy dog."))
print(reverse_string_words2("Python Exercises."))

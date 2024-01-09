def find(lst):
    l_word = ""
    l_length = 0
    for i in lst:
        if len(i) > l_length:
            l_word = i
            l_length = len(i)
    return l_word, l_length


longest_word, length_of_longest = find(["PHP", "Exercises", "Backend"])
print("Longest word:", longest_word)
print("Length of the longest word:", length_of_longest)

longest_word, length_of_longest = find(["apple", "banana", "orange", "watermelon", "kiwi"])
print("Longest word:", longest_word)
print("Length of the longest word:", length_of_longest)

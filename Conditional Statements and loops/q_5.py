def reverse_word(word):
    for char in range(len(word) - 1, -1, -1):
        print(word[char], end="")
    print()
    print(word[::-1])
    print(''.join(reversed(word)))


reverse_word(input("Enter a word: "))

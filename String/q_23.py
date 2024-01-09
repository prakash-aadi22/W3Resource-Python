str1 = 'Python Exercises\n'
print(str1)
print(str1.rstrip())

print("=======================")

text_with_newline = "This is a sentence with a newline character.\n"
text_without_newline = text_with_newline.rstrip("\n")

print("Original text:")
print(text_with_newline)
print(repr(text_with_newline))
print("Text after removing newline:")
print(repr(text_without_newline))

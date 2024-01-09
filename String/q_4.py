def change(str1):
    first_char = str1[0]
    str1 = first_char + str1[1:].replace(first_char, '$')
    return str1


print(change('restart'))
print(change('hello'))
print(change('sam'))
print(change('ssss'))
print(change('intellij idea'))
print(change('dam dam'))
print(change('pycharm'))
print(change('i am a pro coder, and i am coding in python '))

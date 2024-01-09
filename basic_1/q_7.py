name = input("Enter the name of your file with extension: ")
f_ex = name.split(".")
print("The extension name is: " + f_ex[-1])
print("The extension name is: " + repr(f_ex[-1]))
print("The extension name is: " + f_ex[-2])
print("The extension name is: " + repr(f_ex[-2]))
# print("The extension name is: " + (f_ex[-3])) # error
# print("The extension name is: " + repr(f_ex[-3])) # error
print("The extension name is: " + (f_ex[0]))
print("The extension name is: " + repr(f_ex[0]))
print("The extension name is: " + (f_ex[1]))
print("The extension name is: " + repr(f_ex[1]))

def change_case(s):
    return s.upper(), s.lower()


upper_case, lower_case = change_case(input("Enter a string: "))
print("In UpperCase: " + upper_case)
print("In LowerCase: " + lower_case)

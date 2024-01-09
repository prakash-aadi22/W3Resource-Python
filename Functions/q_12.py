def palindrome(s):
    s2 = s.replace(" ", "")
    s1 = "".join(reversed(s2))
    if s1 == s2:
        print(s, "is a palindrome.")
    else:
        print(s, "is not a palindrome.")


palindrome("madam")
palindrome("nurses run")
palindrome("aza")
palindrome("sa")
palindrome("s")

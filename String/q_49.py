def vowel(s):
    vowels = "aeiouAEIOU"
    print([v for v in s if v in vowels])
    print(len([v for v in s if v in vowels]))
    print((v for v in s if v in vowels))
    print({v for v in s if v in vowels})
    print(len({v for v in s if v in vowels}))


vowel('w3resource')

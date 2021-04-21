def print_vowel(sentence1,sentence2):

    lowercase1 = list(sentence1.lower())
    lowercase2 = list(sentence2.lower())

    for x in lowercase1:
        for y in lowercase2:
            if x==y:            #comapre index of strings
                print(x)


print_vowel('house','compputers')
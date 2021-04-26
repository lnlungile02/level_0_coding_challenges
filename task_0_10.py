def print_vowel(sentence1,sentence2):

    lowercase1 = set(sentence1.lower())
    lowercase2 = set(sentence2.lower())

    common_letters=lowercase1 & lowercase2
    print("Common letters:"+str(common_letters))



print_vowel('house','computers')

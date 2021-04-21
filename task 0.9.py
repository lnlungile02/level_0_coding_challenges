def print_vowel(sentence):

    lowercase = list(sentence.lower()) #convert string to lowercase

    vowel=["a","e","i","o","u"]
    for x in lowercase:
        for y in vowel:
            if x==y: #compare indexes to see if vowel is present
                print(x)


print_vowel('LUNGILE MINENHLE NJAKAZI')
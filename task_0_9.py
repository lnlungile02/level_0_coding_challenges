def print_vowel(sentence):

    lowercase = set(sentence.lower()) #convert string to lowercase
    vowels_in_sentence=[]
    vowel=["a","e","i","o","u"]
    for x in lowercase:
        for y in vowel:
            if x==y: #compare indexes to see if vowel is present
                vowels_in_sentence.append(x)
    
    print("Vowels:"+str(vowels_in_sentence))


print_vowel('LUNGILE MINENHLE NJAKAZI')

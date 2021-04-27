def print_vowel(sentence):

    lowercase = set(sentence.lower()) 
    vowels_in_sentence=[]
    vowel=["a","e","i","o","u"]
    for x in lowercase:
        for y in vowel:
            if x==y: 
                vowels_in_sentence.append(x)
    
    print("Vowels:"+str(vowels_in_sentence))


print_vowel('LUNGILE MINENHLE NJAKAZI')

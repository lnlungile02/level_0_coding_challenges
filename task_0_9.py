def print_vowel(sentence):

    lowercase = set(sentence.lower()) 
    vowels_in_sentence=[]
    vowel=["a","e","i","o","u"]
    string_vowels = ""
    for x in lowercase:
        for y in vowel:
            if x==y: 
                vowels_in_sentence.append(x)
    
    return("Vowels: "+ string_vowels+ ", ".join(vowels_in_sentence))


print(print_vowel('LUNGILE MINENHLE NJAKAZI'))

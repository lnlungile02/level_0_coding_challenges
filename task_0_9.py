def print_vowel(sentence):

    lowercase = set(sentence.lower())
    vowels_in_sentence = []
    vowel = ["a", "e", "i", "o", "u"]
    string_vowels = ""
    for x in lowercase:
        for y in vowel:
            if x == y:
                vowels_in_sentence.append(x)
    sentence = string_vowels + ", ".join(vowels_in_sentence)
    return f"Vowels: {sentence}"


def main():
    print(print_vowel("Eckard Berry"))


if __name__ in "__main__":
    main()

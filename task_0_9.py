def print_vowel(sentence):

    letters = set(sentence.lower())
    vowels_in_sentence = []
    vowels = ["a", "e", "i", "o", "u"]

    for char in letters:
        for vowel in vowels:
            if char == vowel:
                vowels_in_sentence.append(char)
    sentence = ", ".join(vowels_in_sentence)
    print(f"Vowels: {sentence}")


def main():
    print_vowel("Eckard Berry")


if __name__ in "__main__":
    main()

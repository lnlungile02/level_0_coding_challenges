def print_vowel(sentence):

    lowercase = set(sentence.lower())
    vowels_in_sentence = []
    vowel = ["a", "e", "i", "o", "u"]

    for x in lowercase:
        for y in vowel:
            if x == y:
                vowels_in_sentence.append(x)
    sentence = ", ".join(vowels_in_sentence)
    print(f"Vowels: {sentence}")


def main():
    print_vowel("Eckard Berry")


if __name__ in "__main__":
    main()

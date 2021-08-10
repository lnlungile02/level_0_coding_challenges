def print_vowel(sentence_one, sentence_two):
    similar_letters = []
    letters_one = list(sentence_one.lower())
    letters_two = list(sentence_two.lower())

    for char_one in letters_one:
        for char_two in letters_two:
            if char_one == char_two:
                similar_letters.append(char_one)

    print("Common letters: " + ", ".join(similar_letters))


def main():
    print_vowel("house", "computers")


if __name__ in "__main__":
    main()

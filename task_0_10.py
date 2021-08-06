def print_vowel(sentence_one, sentence_two):
    similar_letters = []
    lowercase_one = list(sentence_one.lower())
    lowercase_two = list(sentence_two.lower())

    for x in lowercase_one:
        for y in lowercase_two:
            if x == y:  # comapre index of strings
                similar_letters.append(x)

    print("Common letters: " + ", ".join(similar_letters))


def main():
    print_vowel("house", "computers")


if __name__ in "__main__":
    main()

def print_vowel(sentence1, sentence2):
    similar_letters = []
    lowercase1 = list(sentence1.lower())
    lowercase2 = list(sentence2.lower())

    for x in lowercase1:
        for y in lowercase2:
            if x == y:  # comapre index of strings
                similar_letters.append(x)

    print("Common letters: " + ", ".join(similar_letters))


def main():
    print_vowel("house", "computers")


if __name__ in "__main__":
    main()

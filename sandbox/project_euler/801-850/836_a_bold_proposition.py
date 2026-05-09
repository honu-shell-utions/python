"""
Jim McCleery
May 9, 2026
Kailua-Kona, HI

Project Euler Problem 836
https://projecteuler.net/problem=836

This program extracts the first letter of each bolded word from the problem
statement and concatenates them to reveal the hidden answer.
"""


def extract_first_letters(phrases):
    """
    Return a string made from the first letter of every word
    in the given list of phrases.
    """
    letters = []

    for phrase in phrases:
        words = phrase.split()

        for word in words:
            letters.append(word[0])

    return "".join(letters)


def main():
    # Bolded phrases from the problem statement.
    bold_phrases = [
        "affine plane",
        "radically integral local field",
        "open oriented line section",
        "jacobian",
        "orthogonal kernel embedding",
    ]

    answer = extract_first_letters(bold_phrases)

    print(answer)


if __name__ == "__main__":
    main()

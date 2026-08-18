print("Задание 2")

def analyze_list(words: list[str]):
    new_words = []
    for word in words:
        if len(word) >= 5:
            new_words.append(word.lower())

    return new_words

words = [
    "Python",
    "java",
    "C++",
    "Rust",
    "Go",
    "Swift",
    "PHP"
]

print(analyze_list(words))
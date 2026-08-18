print("Задание 4")
def longest_word(text):
    
    if not text:
        return None

    full_text = text.split()

    long_word = full_text[0]
    for word in full_text:
        if len(word) > len(long_word):
            long_word = word

    return long_word

print(longest_word(""))
print(longest_word("Я учусь программировать на языке Python"))
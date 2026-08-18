print("Задание 3")
def  is_palindrome(text):
    clean_text = ("".join(text.split())).lower()
    inverted = clean_text[::-1]
    if clean_text == inverted:
        return True
    else:
        return False

print(is_palindrome("Анна"))
print(is_palindrome("Ання"))
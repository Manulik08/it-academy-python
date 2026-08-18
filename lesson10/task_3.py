print("Задание 3")

def text_operation(text: str):
    final_text = text.replace(" ", "")
    appearances = {}
    for symbol in final_text:
        if not symbol in appearances:
            appearances[symbol] = {"quantity": 0}
        if symbol in appearances:
            appearances[symbol]["quantity"] += 1

    return appearances

text = "functional programming"

print(text_operation(text))

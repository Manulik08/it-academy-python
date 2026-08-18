print("Задание 1")
from statistics import mean
def analyze_grades(*grades):
    if not grades:
        return None

    count = len(grades)
    average = round(mean(grades), 2)
    highest = max(grades)
    lowest = min(grades)
    passed = 0
    for grade in grades:
        if grade >= 60:
            passed += 1

    return {
        "count": count,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "passed": passed
    }
result = analyze_grades(5, 8, 61)
print(result)
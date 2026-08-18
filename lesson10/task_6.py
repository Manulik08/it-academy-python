print("Задание 6")

students = [
{"name": "Иван", "score": 82},
{"name": "Анна", "score": 95},
{"name": "Петр", "score": 67},
{"name": "Мария", "score": 91},
{"name": "Олег", "score": 73},
{"name": "Елена", "score": 88},
]

high_scores = [student for student in students if student["score"] >= 80]

sorted_scores = sorted(high_scores, key = lambda x: x["score"], reverse=True)

for student in sorted_scores:
    print(f"{student["name"]} ({student["score"]})")






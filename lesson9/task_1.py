print("Задание 1")

def analyze_logins(logs: list[tuple[str, bool]]):
    result = {}
    for user, is_success in logs:
        if user not in result:
            result[user] = {"success": 0, "failed": 0}
        if is_success:
            result[user]["success"] += 1
        else:
            result[user]["failed"] += 1
    return result

logs = [
("alice", True),
("bob", False),
("alice", True),
("alice", False),
("bob", True),
("charlie", False),
]

print(analyze_logins(logs))
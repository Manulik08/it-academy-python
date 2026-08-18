print("Задание 1")

def find_file(folder: dict, target_filename: str) -> str | None:
    for obj in folder.keys():
        if isinstance(folder[obj], dict):
            current_path = find_file(folder[obj], target_filename)
            if current_path:
                return f"{obj}/{current_path}"
        elif obj == target_filename:
            return obj
    return None


file_system = {
    "project_notes1.txt": "content",
    "documents": {
        "work": {
            "project_notes.txt": "content",
            "budget.xlsx": "content"
        },
        "personal": {
            "passport.pdf": "content"
        }
    },
    "photos": {
        "vacation.jpg": "content"
    }
}

print(find_file(file_system, "project_notes.txt"))
print(find_file(file_system, "passport.pdf"))


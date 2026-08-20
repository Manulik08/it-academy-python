print("Задание 3")

import os
files = os.listdir("project")
txt_files = []
for i in files:
    if i.endswith("txt"):
        txt_files.append(i)
print(f"Файлы с расширением txt:")
for file in txt_files:
    print(file)
print(f"Количество файлов с расширением txt: {len(txt_files)}")
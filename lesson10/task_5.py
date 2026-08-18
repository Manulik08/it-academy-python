print("Задание 5")

files = [
"main.py",
"test.py",
"README.md",
"data.csv",
"notes.txt"
]

#  1) способ с функцией

def files_py(files):
    return files.endswith("py")

python_files = list(filter(files_py, files))
print(python_files)


# 2) способ с lambda

python_files_lambda = list(filter(lambda x: x.endswith("py"), files))
print(python_files_lambda)
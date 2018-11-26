import string
import math

#print(zero(-5))

# file = open('test.txt', "w")
# file.write("Hello, file")
# file.close()

# with open("test.txt", "r") as file:
#     count = 0
#     for line in file:
#         print(str(count), "line as", line)
#         count += 1
#
#         if "world" in line:
#             print("Found a word")
#return line(len(key) + 1; -1)

def set_value(key: str, value: str) -> None:
    # Функция добавляет пользователя в файл database.txt
    with open("database.txt", "a") as file:
        file.write(f"{key}:{value}\n")
    return None


def get_value(key: str) -> str:
    # Функция возвращает значение по ключу
    with open("database.txt", "r") as file:
        for line in file:
            if key == line.split(":")[0]:
                return line.split(":")[1].replace("\n", "")

def new_base(size: int) -> None:
    # Функция заполняет файл database.txt пользователями
    for num in range(size):
        set_value(f"user{num}", f"pass{num}")
#print(get_value("user1"))
#new_base(30)
#
# with open("database.txt", "a") as file:  # open for append
#     for line in open("database.txt", "r"):
#         line = line.replace('user1', 'word')
#         file.write(line)
# with open("database.txt", "w") as file:
#   print()
with open("database.txt", "r") as file:
    text = file.read()

with open("database.txt", "w") as file:
    file.write(text.replace("user1:", "row:"))
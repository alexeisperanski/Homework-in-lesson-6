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
    with open("database.txt", "a") as file:
        file.write(key + ':' + value + "\n")
    return None


def get_value(key: str) -> str:
    with open("database.txt", "r") as file:
        for line in file:
            if key == line.split(":")[0]:
                return line.split(":")[1].replace("\n", "")


#for i in range(100):
#    set_value('user' + str(i),'pass' + str(i))
print(get_value("user1"))
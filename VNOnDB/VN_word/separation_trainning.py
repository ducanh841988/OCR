
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

all_line = []
with open("groundtruth.txt", "r") as ins:
    for line in ins:
        all_line.append(line)

writer = open("train_file.txt", "w")
with open("train_set.txt", "r") as ins:
    for line in ins:
        name = line[: len(line) - 8]
        for line in all_line:
            if name in line:
                writer.write(line)
writer.close()

writer = open("validation_file.txt", "w")
with open("validation_set.txt", "r") as ins:
    for line in ins:
        name = line[: len(line) - 8]
        for line in all_line:
            if name in line:
                writer.write(line)
writer.close()

writer = open("test_file.txt", "w")
with open("test_set.txt", "r") as ins:
    for line in ins:
        name = line[: len(line) - 8]
        for line in all_line:
            if name in line:
                writer.write(line)
writer.close()
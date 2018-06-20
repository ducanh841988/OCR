
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
vocab = []

#with open("vn_list_unicode.txt", "r") as ins:
#    vocab = ins.readlines()
#for s in vocab:
#    print s.encode("utf-8")
max_len = 0
max_word = ""
writer = open("groundtruth_new.txt", "w")
with open("groundtruth.txt", "r") as ins:
    for line in ins:
        if len(line) > 2:
            arr = line.split()
            str = arr[1].decode('utf8')
            if max_len < len(str):
                max_len = len(str)
                max_word = str
            writer.write(line)


writer.close()
print (max_len, max_word)
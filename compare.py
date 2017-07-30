# coding: UTF-8

import re

file1 = open('result.txt','r')
file2 = open('e:/school.txt', 'a+')

f1 = file1.readlines()
f1arr = []
f2arr = []
f2 = file2.readlines()
num = 0
for line_1 in f1:
    judge = True
    for line_2 in f2:
        lines1 = re.split(' ', line_1)
        lines2 = re.split(' ', line_2)
        if lines1[0] == lines2[0]:
            judge = False
            break
    if judge:
        file2.write(line_1)
        num += 1


print '共加入：%d' % num
file2.close()
file1.close()
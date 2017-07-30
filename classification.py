# coding: UTF-8
import re

files = open('e:/url.txt','r')
gov = open('e:/gov.txt','a+')
news = open('e:/news.txt','a+')
new_file = open('e:/compary.txt','a+')
gov_num = 0
news_num = 0
com_num = 0
lines = files.readlines()
for line in lines:
    if re.search('gov',line):
        gov_num += 1
        gov.write(line)
    elif re.search('媒体',line) or re.search('新闻',line) or re.search('传媒',line):
        news_num += 1
        news.write(line)
    else:
        com_num += 1
        new_file.write(line)

print '政府：%d' % gov_num
print '媒体：%d' % news_num
print '企业：%d' % com_num
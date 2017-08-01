# coding=utf8
import urllib2
import string
import urllib
import re
import random

def baidu_search(keyword,pn):
    p= {'wd': keyword}
    res=urllib2.urlopen(("http://www.baidu.com/s?"+urllib.urlencode(p)+"&pn={0}&cl=3&rn=100").format(pn))
    html=res.read()
    return html
def getList(regex,text):
    arr = []

    res = re.findall(regex, text)
    if res:
        for r in res:
            r[1].decode('utf-8')
            arr.append(r)
    return arr



def geturl(keyword, pages):
    sums = 0
    for page in range(pages):
        pn = page*10 + 1
        html = baidu_search(keyword,pn)
        arrList = getList("none;\">(w+\..*)\/&nbsp;<\/a>.*data-tools='\{\"title\":\"(.*)\",\"url", html)
        sums += len(arrList)
        save = open('result.txt', 'a+')
        for one in arrList:
            new = one[1].split('"')
            strs = one[0] + " " + new[0] + "\n"
            save.write(strs)
    print "共有：%d" % sums


if __name__=='__main__':
    keyword = raw_input('请输入搜索关键字：')
    pages = raw_input('请输入需要搜索的页数：')
    pages = int(pages)
    geturl(keyword, pages)
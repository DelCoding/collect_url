main.py --> 可以自动的提取百度搜索出来的url和title，并保存在result.txt；

preg.py --> 用来提取本地的google搜索页面，使用时需要手动的将google搜索结果的页面保存在html.txt，然后运行脚本就会自动提取其中的url和title；

classification.py --> 用来将所有的url进行分类，利用目标url或title的特性进行分类；

compare.py --> 将对比两个文件中的url有无重复，如果url不存在则写入进去，否则不写入。

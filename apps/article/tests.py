from django.test import TestCase

# Create your tests here.
def clean_path(full_path):
    path = str(full_path)
    if 'page=' in path:
        """
        对数据进行清洗，包括两种情况，第一个是page以？开头，第二个是page以&开头
        字符串索引index(page)返回p的位置，减一得到？或者&的位置，切片去掉
        """
        path = path[:path.index('page=')-1]
        print(path)
    path += '&' if '/search/' in path else '?'
    # print(path)
    return path
"""
主页
/?page=2
搜索
/article/search/?keyword=%E4%BD%A0%E5%A5%BD
分类
/article/category/%E5%AD%A6%E4%B9%A0/?page=3
"""
print(clean_path('/article/category/%E5%AD%A6%E4%B9%A0/?page=3'))
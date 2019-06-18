import re

s = 'Alex:1994,Sunny:1993'
pattern = r'\w+:\d+'

l = re.findall(pattern, s)
print(l)

pattern = r'(\w+):(\d+)'
# 只读取元组

# re模块调用findall
l = re.findall(pattern, s)
print(l)

# 使用compile对象调用
regex = re.compile(pattern)
# l=regex.findall(s)
l = regex.findall(s, 0, 10)

print(l)

# 按照匹配内容切割字符串
l = re.split(r':|,', s)
# l=re.split(r'[:,]',s)
print(l)

# 替换匹配到的内容
s = re.sub(r'\s+', '#', 'this is a test')
print(s)
s = re.sub(r'\s+', '#', 'this is a test', 2)
print(s)
s = re.subn(r'\s+', '#', 'this is a test', 2)
print(s)

# 练习，提取一段文字中所有的日期（2019-05-23）
# 将日期打出来，格式为2019/05/23
s = 'fjowijfioj(2019-05-23)iefjijoiqoi(2070-09-02)ff61456'
pattern = r'(\d{4}-\d{2}-\d{2})'
l = re.findall(pattern, s)
print(l)
for i in l:
    k = re.sub(r'-+', '/', i)
    print(k)

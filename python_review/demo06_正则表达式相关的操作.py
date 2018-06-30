"""
正则表达式：用来描述,匹配某个语法规则的字符串..作用用来检索,替换那些匹配某个模式的文本
re 模块操作：在Python中需要通过正则表达式对字符串进行匹配的时候，可以使用一个模块，名字为re
re模块的使用过程:
    导入re模块
        import re
    使用match或search方法进行匹配操作
        result=re.match(正则表达式,匹配以指定正则表达式开头的字符串)
    如果上一步匹配数据的话,可以使用group方法提取数据
        result.group()
    re.match或re.search是用来进行正则匹配检查的方法，若字符串匹配正则表达式，则match或search方法返回匹配对象（Match Object），否则返回None（注意不是空字符串""）。
    匹配对象Macth Object具有group方法，用来返回字符串的匹配部分。

正则表达式的单字符匹配
.                   匹配任意一个字符(除了\n)
\d                  匹配数字,即0-9
[]                  匹配[]中列举的字符
\s                  匹配空白,即空格,tab键
\w                  匹配单词字符,即a-z,A-Z,0-9


表示数量:匹配多个字符的相关格式
*                   匹配前一个字符出现0次或者无限次
+                   匹配前一个字符出现1次或者无限次
?                   匹配前一个字符出现一次或者0次
{m}                 匹配前一个字符出现m次
{m,}                匹配前一个字符至少出现m次
{m,n}               匹配前一个字符出现从m次到n次
"""

import re
#1.匹配出0-99之间的数

print(re.search(r"[1-9]?\d","90").group())

#2.需求：匹配出，8到20位的密码，可以是大小写英文字母、数字、下划线
ret = re.match(r".{8,20}", "1ad12f23s34455ff66")
print(ret.group())


"""
匹配分组
字符                  功能
|                     匹配左右任意一个表达式
(ab)                  将括号中的字符作为一个分组
(?P<name>)            分组起别名
(?P=name)             引用别名为name分组匹配到的字符串
"""
#3.切割字符串  :正则表达式的分割:split(字符串的分割功能没有正则表达式强大)
str = "hello,java python:world"
res=re.split(r",| |:",str)
print(res)


#4.匹配163, 126, qq邮箱之间的数字
print(re.search(r"\w{4,20}@(163|126|qq)\.com", "1315382986@qq.com").group())

"tel=15938710594"
#5.匹配上面的字符串, 并且提取等号左边的值
print(re.search(r"([a-zA-Z]+)=([1-9]\d+)", "tel=15938710594").group(1))

#6.匹配出 < html > hh < / html >
data="<html>hello world</html>"
res=re.match(r"<(?P<name>\w+)>.*</(?P=name)>",data)
print(res.group())

#<html>hello world</html>匹配出hello world
res=re.findall(r"<html>(.*?)</html>",data)
print(res[0])

#python贪婪和非贪婪

#Python里数量词默认是贪婪的（在少数语言里也可能是默认非贪婪），总是尝试匹配尽可能多的字符
s = "This is a number 234-235-22-423"
r = re.match(".+(\d+-\d+-\d+-\d+)", s)
print(r.group(1))
#'4-235-22-423'(贪婪模式: 在满足后面的正则表达式的前提下, .+匹配越多越好)
r = re.match(".+?(\d+-\d+-\d+-\d+)", s)
print(r.group(1))
#'234-235-22-423'(非贪婪模式: 在满足后面的正则表达式的前提下, .+匹配越少越好)
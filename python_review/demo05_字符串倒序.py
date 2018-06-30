#字符串倒叙
str="helloworld"
#方法一：使用切片
print(str[::-1])
#方法二：将字符串转化为字典利用其reverse()方法
list_str=list(str)
list_str.reverse()
print("".join(list_str))
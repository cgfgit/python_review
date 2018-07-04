#写一个匿名函数，实现1-10（不包含10）的平方。
a=lambda n:[i*i for i in range(10)]
print(a(10))


#求出1-100内奇数的和
# a=[i for i in range(100)if i%2==1]
from functools import reduce
result=reduce(lambda x,y:x+y,[i for i in range(100) if i % 2 == 1])
print(result)

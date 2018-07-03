#函数的打包
"""

    :param a:
    :param b:
    :param args: *修饰的args可以接收多个未命名的参数,args是元组类型
    :param kwargs: **修饰kwargs可以几首多个命名的参数,kwargs是字典类型
    """
def pack(a,b,*args,**kwargs):
    print("a={}".format(a))
    print("b={}".format(b))
    print("args={}".format(args))
    print("kwargs={}".format(kwargs))
pack(1,2)
pack(1,2,3)
pack(1,2,3,4)
print("*"*10)
pack(1,2,3,"hello",num1=1,num2=2)

#函数的解包
def unpack(num1,num2):
    print("num1+num2={}".format(num1+num2))
t1=(100,200)
d1={"num1":500,"num2":600}
unpack(*t1)             #解包：展开  unpack(100,200)
unpack(**d1)            # 解包：展开  unpack("num1"=500,"num2"=600)

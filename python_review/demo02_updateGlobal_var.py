"""
修改全局变量：
函数内部修改全局变量：若是可变类型，可以不用global关键字声明
                　　若是不可变类型,修改全局变量需要用global关键字声明
                
"""
#若是不可变类型,修改全局变量需要用global关键字声明
a=10
def add():
    global a
    a+=10
    print("a={}".format(a))
add()


#可变类型修改局部变量不用global关键字声明

list=[100]
def list_add():
    list[0]+=list[0]
    print(list[0])
list_add()

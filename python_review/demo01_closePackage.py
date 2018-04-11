"""
闭包：至少有两个函数,且外层函数嵌套内层函数
    　内层函数可能用到外层函数的参数
      外层函数的返回值是内层函数的函数对象
"""
def outter(out_num):
    def inner(in_num):
        print("相加结果为:{}".format(out_num+in_num))
    return inner

fun=outter(100)
fun(50)


#闭包内层函数改变外层函数的参数
def set_counter(num):
    def counter():
        nonlocal num
        num+=1
        print(num)
    return counter

c=set_counter(100)
c()
c()



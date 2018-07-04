#函数内部的变量名如果第一次出现，且出现在=前面，即被视为定义一个局部变量.会将全局变量覆盖
num = 100
def func():
    num = 123
    print(num)
func()                  #out:123

print("*" * 100)


"""
num1 = 100
def func():
    num1 += 100
    print(num1)
func()

out：
UnboundLocalError: local variable 'num' referenced before assignment

错误提示局部变量num在赋值前被应用，也就是该变量没有定义就使用它，由此再次证明了这里定义了一个局部变量，
而不是使用的全局的num。
"""


"""
函数内部的变量名如果第一次出现，且出现在=后面，且该变量在全局域中已定义，则这里将引用全局变量，
如果该变量在全局域中没有定义，当然会出现“变量未定义”的错误。例如
"""
num2 = 100
def func():
    x = num2 + 100
    print(x)
func()
print("*"*100)


"""
在函数中，如果想给全局变量赋值，则需要用关键字global生命，例如：
"""
num3 = 100
def func():
    global num3
    num3 = 500
    print(num3)
func()

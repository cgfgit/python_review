# 斐波那契数列
# 方法１,使用列表实现
def fibonacci(num):
    fibs = [1, 2]
    for i in range(num - 2):
        fibs.append(fibs[-1] + fibs[-2])  # 将倒数第一个和倒数第二个值相加追加到列表中
    return fibs


result = fibonacci(5)
print(result)

"""
2) 用Fib(n)表示青蛙跳上n阶台阶的跳法数，青蛙一次性跳上n阶台阶的跳法数1(n阶跳)，设定Fib(0) = 1；

当n = 1 时， 只有一种跳法，即1阶跳：Fib(1) = 1;

当n = 2 时， 有两种跳的方式，一阶跳和二阶跳：Fib(2) = Fib(1) + Fib(0) = 2;

当n = 3 时，有三种跳的方式，第一次跳出一阶后，后面还有Fib(3-1)中跳法； 第一次跳出二阶后，后面还有Fib(3-2)中跳法；第一次跳出三阶后，后面还有Fib(3-3)中跳法

Fib(3) = Fib(2) + Fib(1)+Fib(0)=4;

当n = n 时，共有n种跳的方式，第一次跳出一阶后，后面还有Fib(n-1)中跳法； 第一次跳出二阶后，后面还有Fib(n-2)中跳法..........................第一次跳出n阶后, 后面还有 Fib(n-n)中跳法.

Fib(n) = Fib(n-1)+Fib(n-2)+Fib(n-3)+..........+Fib(n-n)=Fib(0)+Fib(1)+Fib(2)+.......+Fib(n-1)

又因为Fib(n-1)=Fib(0)+Fib(1)+Fib(2)+.......+Fib(n-2)

两式相减得：Fib(n)-Fib(n-1)=Fib(n-1) =====》 Fib(n) = 2*Fib(n-1) n >= 2


"""


def jump(num):
    if (num == 0 | num == 1):
        return 1
    else:
        return 2 * jump(num - 1)


result = jump(3)
print(result)
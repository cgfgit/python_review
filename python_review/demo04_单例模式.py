"""
确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，这个类称为单例类
__new__方法:使用类名()创建对象时候,python解释器首先会调用__new__方法为对象分配空间
__new__是一个由object基类提供的内置静态方法,主要作用有两个:
1.在内存中为对象分配空间
2.返回对象的引用
__init__作用:
1.	对象初始化
2.	定义实例属性

"""
#单例模式

class Recycle(object):
    instance=None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance=super().__new__(cls)
        return cls.instance
    def __int__(self):
        print("对对象进行初始化")
r1=Recycle()
print(r1)
r2=Recycle()
print(r2)
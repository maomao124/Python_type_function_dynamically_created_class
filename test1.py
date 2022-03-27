"""
 * Project name(项目名称)：Python_type函数_动态创建类
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/27 
 * Time(创建时间)： 13:56
 * Version(版本): 1.0
 * Description(描述)：
 type(obj)
type(name, bases, dict)

第一种语法格式用来查看某个变量（类对象）的具体类型，obj 表示某个变量或者类对象。
第二种语法格式用来创建类，其中 name 表示类的名称；bases 表示一个元组，其中存储的是该类的父类；dict 表示一个字典，用于表示类内定义的属性或者方法。
 """


class T:
    def f1(self):
        print("hello")


# 定义一个实例方法
def say(self):
    print("你好")


if __name__ == '__main__':
    print(type(12))
    print(type(1.1))
    print(type('123'))
    print(type(T))
    t = T()
    print(type(t))

    C = type("C", (T, object), dict(say=say, name="张三"))
    c = C()
    c.say()
    c.f1()
    print(c.name)

## Python装饰器

装饰器用于在源码中“标记”函数，以增强函数的行为。

现有一个求和函数add，现在要求统计函数执行的时长:
```
def add(a, b):
    print(a+b)
```

最low的做法：
```
def add(a, b):
    start = time.time()
    print(a + b)
    time.sleep(2)#模拟耗时操作
    long = time.time() - start
    print(f'共耗时{long}秒。')
```

对原函数做了修改，不仅增加了耦合性，扩展和复用也变得难以实现。

我们可以这样写：
```
def timer(func,*args):
    start = time.time()
    func(*args)
    time.sleep(2)#模拟耗时操作
    long = time.time() - start
    print(f'共耗时{long}秒。')

timer(add,1,2)
```

这样没有改变原函数吧？是的，但是改变了函数调用方式，每个调用add的地方都需要修改，这么做只是转嫁了矛盾而已。

又不能修改原函数，又不能改变调用方式，那该怎么办呢？装饰器是时候登场了。

在写装饰器之前先了解两个概念：高阶函数和闭包

高阶函数：接受函数为入参，或者把函数作为结果返回的函数。后者称之为嵌套函数。

闭包：指延伸了作用域的函数，其中包含函数定义体中引用、但是不在定义体中定义的非全局变量。概念比较晦涩，简单来说就是嵌套函数引用了外层函数的变量。

嵌套函数和闭包可以理解为是同时存在的，上面的timer已经是高阶函数了，它接受函数作为入参，我们把它改造为嵌套函数实现装饰器：
```
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs) #此处拿到了被装饰的函数func
        time.sleep(2)#模拟耗时操作
        long = time.time() - start
        print(f'共耗时{long}秒。')
    return wrapper #返回内层函数的引用
@timer
def add(a, b):
    print(a+b)

add(1, 2) #正常调用add
```
timer被我们改造成了装饰器，它接受被装饰函数为入参，返回内部嵌套函数的引用（注意：此处并未执行函数），内部嵌套函数wrapper持有被装饰函数的引用即func。

“@”是Python的语法糖，它的作用类似于：
```
add = timer(add) #此处返回的是timer.<locals>.wrapper函数引用
add(1, 2)
```

装饰器的加载到执行的流程：

模块加载 ->> 遇到@，执行timer函数，传入add函数 ->> 生成timer.<locals>.wrapper函数并命名为add，其实是覆盖了原同名函数 ->> 调用add(1, 2) ->> 去执行timer.<locals>.wrapper(1, 2) ->> wrapper内部持有原add函数引用(func)，调用func(1, 2) ->>继续执行完wrapper函数

理解了装饰器之后，我们可以思考一下，带参数的装饰器该怎么写呢？

我们知道装饰器最终返回的是嵌套函数的引用，只要记住这点，装饰器就任由我们发挥了。写一个带参数的装饰器：
```
def auth(permission):
    def _auth(func):
        def wrapper(*args, **kwargs):
            print(f"验证权限[{permission}]...")
            func(*args, **kwargs)
            print("执行完毕...")

        return wrapper

    return _auth

@auth("add")
def add(a, b):
    """
    求和运算
    """
    print(a + b)


add(1, 2)  # 正常调用add
```



----------------------
生成器
----------------------
我们可以通过yield关键字创建一个生成器，每次我们调用的时候执行到yield关键字处则停止。下次再次调用则还是从yield处开始往下执行：
# Generators help you make lazy code.
def double_numbers(iterable):
    for i in iterable:
        yield i + i

# Generators are memory-efficient because they only load the data needed to
# process the next value in the iterable. This allows them to perform
# operations on otherwise prohibitively large value ranges.
# NOTE: `range` replaces `xrange` in Python 3.
for i in double_numbers(range(1, 900000000)):  # `range` is a generator.
    print(i)
    if i >= 30:
        break
复制代码
除了yield之外，我们还可以使用()小括号来生成一个生成器：
# Just as you can create a list comprehension, you can create generator
# comprehensions as well.
values = (-x for x in [1,2,3,4,5])
for x in values:
    print(x)  # prints -1 -2 -3 -4 -5 to console/terminal

# You can also cast a generator comprehension directly to a list.
values = (-x for x in [1,2,3,4,5])
gen_to_list = list(values)
print(gen_to_list)  # => [-1, -2, -3, -4, -5]
复制代码
关于生成器和迭代器更多的内容，可以查看下面这篇文章：
五分钟带你弄懂迭代器与生成器，夯实代码能力
----------------
装饰器
------------------------
我们引入functools当中的wraps之后，可以创建一个装饰器。装饰器可以在不修改函数内部代码的前提下，在外面包装一层其他的逻辑:
# Decorators
# In this example `beg` wraps `say`. If say_please is True then it
# will change the returned message.
from functools import wraps

def beg(target_function):
    @wraps(target_function)
    # 如果please为True，额外输出一句Please! I am poor :(
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg

    return wrapper

@beg
def say(say_please=False):
    msg = "Can you buy me a beer?"
    return msg, say_please

print(say())                 # Can you buy me a beer?
print(say(say_please=True))  # Can you buy me a beer? Please! I am poor :(
复制代码
装饰器之前也有专门的文章详细介绍，可以移步下面的传送门：
一文搞定Python装饰器，看完面试不再慌
------------------------
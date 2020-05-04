判断语句
---------------
Python当中的判断语句非常简单，并且Python不支持switch，所以即使是多个条件，我们也只能罗列if-else。
# Let's just make a variable
some_var = 5

# Here is an if statement. Indentation is significant in Python!
# Convention is to use four spaces, not tabs.
# This prints "some_var is smaller than 10"
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:    # This elif clause is optional.
    print("some_var is smaller than 10.")
else:                  # This is optional too.
    print("some_var is indeed 10.")
复制代码
----------------
循环
----------------
我们可以用in来循环迭代一个list当中的内容，这也是Python当中基本的循环方式。

"""
For loops iterate over lists
prints:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))
复制代码
如果我们要循环一个范围，可以使用range。range加上一个参数表示从0开始的序列，比如range(10)，表示[0, 10)区间内的所有整数：
"""
"range(number)" returns an iterable of numbers
from zero to the given number
prints:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)
复制代码
如果我们传入两个参数，则代表迭代区间的首尾。
"""
"range(lower, upper)" returns an iterable of numbers
from the lower number to the upper number
prints:
    4
    5
    6
    7
"""
for i in range(4, 8):
    print(i)
复制代码
如果我们传入第三个元素，表示每次循环变量自增的步长。
"""
"range(lower, upper, step)" returns an iterable of numbers
from the lower number to the upper number, while incrementing
by step. If step is not indicated, the default value is 1.
prints:
    4
    6
"""
for i in range(4, 8, 2):
    print(i)
复制代码
如果使用enumerate函数，可以同时迭代一个list的下标和元素：
"""
To loop over a list, and retrieve both the index and the value of each item in the list
prints:
    0 dog
    1 cat
    2 mouse
"""
animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)
复制代码
while循环和C++类似，当条件为True时执行，为false时退出。并且判断条件不需要加上括号：
"""
While loops go until a condition is no longer met.
prints:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1  # Shorthand for x = x + 1
复制代码
------------------
捕获异常
------------------
Python当中使用try和except捕获异常，我们可以在except后面限制异常的类型。如果有多个类型可以写多个except，还可以使用else语句表示其他所有的类型。finally语句内的语法无论是否会触发异常都必定执行：
# Handle exceptions with a try/except block
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass                 # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass                 # Multiple exceptions can be handled together, if required.
else:                    # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")   # Runs only if the code in try raises no exceptions
finally:                 #  Execute under all circumstances
    print("We can clean up resources here")
复制代码
-------------------
with操作
--------------------
在Python当中我们经常会使用资源，最常见的就是open打开一个文件。我们打开了文件句柄就一定要关闭，但是如果我们手动来编码，经常会忘记执行close操作。并且如果文件异常，还会触发异常。这个时候我们可以使用with语句来代替这部分处理，使用with会自动在with块执行结束或者是触发异常时关闭打开的资源。
以下是with的几种用法和功能：
# Instead of try/finally to cleanup resources you can use a with statement
# 代替使用try/finally语句来关闭资源
with open("myfile.txt") as f:
    for line in f:
        print(line)

# Writing to a file
# 使用with写入文件
contents = {"aa": 12, "bb": 21}
with open("myfile1.txt", "w+") as file:
    file.write(str(contents))        # writes a string to a file

with open("myfile2.txt", "w+") as file:
    file.write(json.dumps(contents)) # writes an object to a file

# Reading from a file
# 使用with读取文件
with open('myfile1.txt', "r+") as file:
    contents = file.read()           # reads a string from a file
print(contents)
# print: {"aa": 12, "bb": 21}

with open('myfile2.txt', "r+") as file:
    contents = json.load(file)       # reads a json object from a file
print(contents)     
# print: {"aa": 12, "bb": 21}
复制代码
------------------
可迭代对象
-----------------
凡是可以使用in语句来迭代的对象都叫做可迭代对象，它和迭代器不是一个含义。这里只有可迭代对象的介绍，想要了解迭代器的具体内容，请移步传送门：
Python——五分钟带你弄懂迭代器与生成器，夯实代码能力
当我们调用dict当中的keys方法的时候，返回的结果就是一个可迭代对象。
# Python offers a fundamental abstraction called the Iterable.
# An iterable is an object that can be treated as a sequence.
# The object returned by the range function, is an iterable.

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)  # => dict_keys(['one', 'two', 'three']). This is an object that implements our Iterable interface.

# We can loop over it.
for i in our_iterable:
    print(i)  # Prints one, two, three
复制代码
我们不能使用下标来访问可迭代对象，但我们可以用iter将它转化成迭代器，使用next关键字来获取下一个元素。也可以将它转化成list类型，变成一个list。
# However we cannot address elements by index.
our_iterable[1]  # Raises a TypeError

# An iterable is an object that knows how to create an iterator.
our_iterator = iter(our_iterable)

# Our iterator is an object that can remember the state as we traverse through it.
# We get the next object with "next()".
next(our_iterator)  # => "one"

# It maintains state as we iterate.
next(our_iterator)  # => "two"
next(our_iterator)  # => "three"

# After the iterator has returned all of its data, it raises a StopIteration exception
next(our_iterator)  # Raises StopIteration

# We can also loop over it, in fact, "for" does this implicitly!
our_iterator = iter(our_iterable)
for i in our_iterator:
    print(i)  # Prints one, two, three

# You can grab all the elements of an iterable or iterator by calling list() on it.
list(our_iterable)  # => Returns ["one", "two", "three"]
list(our_iterator)  # => Returns [] because state is saved
复制代码
-----------------------
函数
-----------------------
使用def关键字来定义函数，我们在传参的时候如果指定函数内的参数名，可以不按照函数定义的顺序传参：
# Use "def" to create new functions
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y  # Return values with a return statement

# Calling functions with parameters
add(5, 6)  # => prints out "x is 5 and y is 6" and returns 11

# Another way to call functions is with keyword arguments
add(y=6, x=5)  # Keyword arguments can arrive in any order.
复制代码
可以在参数名之前加上*表示任意长度的参数，参数会被转化成list：
# You can define functions that take a variable number of
# positional arguments
def varargs(*args):
    return args

varargs(1, 2, 3)  # => (1, 2, 3)
复制代码
也可以指定任意长度的关键字参数，在参数前加上**表示接受一个dict：
# You can define functions that take a variable number of
# keyword arguments, as well
def keyword_args(**kwargs):
    return kwargs

# Let's call it to see what happens
keyword_args(big="foot", loch="ness")  # => {"big": "foot", "loch": "ness"}
复制代码
当然我们也可以两个都用上，这样可以接受任何参数：
# You can do both at once, if you like
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""
复制代码
传入参数的时候我们也可以使用*和**来解压list或者是dict：
# When calling functions, you can do the opposite of args/kwargs!
# Use * to expand tuples and use ** to expand kwargs.
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)            # equivalent to all_the_args(1, 2, 3, 4)
all_the_args(**kwargs)         # equivalent to all_the_args(a=3, b=4)
all_the_args(*args, **kwargs)  # equivalent to all_the_args(1, 2, 3, 4, a=3, b=4)
复制代码
Python中的参数可以返回多个值：
# Returning multiple values (with tuple assignments)
def swap(x, y):
    return y, x  # Return multiple values as a tuple without the parenthesis.
                 # (Note: parenthesis have been excluded but can be included)
x = 1
y = 2
x, y = swap(x, y)     # => x = 2, y = 1
# (x, y) = swap(x,y)  # Again parenthesis have been excluded but can be included.
复制代码
函数内部定义的变量即使和全局变量重名，也不会覆盖全局变量的值。想要在函数内部使用全局变量，需要加上global关键字，表示这是一个全局变量：
# Function Scope
x = 5
def set_x(num):
    # Local var x not the same as global variable x
    x = num    # => 43
    print(x)   # => 43
def set_global_x(num):
    global x
    print(x)   # => 5
    x = num    # global var x is now set to 6
    print(x)   # => 6
set_x(43)
set_global_x(6)
复制代码
Python支持函数式编程，我们可以在一个函数内部返回一个函数：
# Python has first class functions
def create_adder(x):
    def adder(y):
        return x + y
    return adder
add_10 = create_adder(10)
add_10(3)   # => 13
复制代码
Python中可以使用lambda表示匿名函数，使用:作为分隔，:前面表示匿名函数的参数，:后面的是函数的返回值：
# There are also anonymous functions
(lambda x: x > 2)(3)                  # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1)  # => 5
复制代码
我们还可以将函数作为参数使用map和filter，实现元素的批量处理和过滤。关于Python中map、reduce和filter的使用，具体可以查看之前的文章：
五分钟带你了解map、reduce和filter
# There are built-in higher order functions
list(map(add_10, [1, 2, 3]))          # => [11, 12, 13]
list(map(max, [1, 2, 3], [4, 2, 1]))  # => [4, 2, 3]
list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # => [6, 7]
复制代码
我们还可以结合循环和判断语来给list或者是dict进行初始化：
# We can use list comprehensions for nice maps and filters
# List comprehension stores the output as a list which can itself be a nested list
[add_10(i) for i in [1, 2, 3]]         # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]
# You can construct set and dict comprehensions as well.
{x for x in 'abcddeef' if x not in 'abc'}  # => {'d', 'e', 'f'}
{x: x**2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

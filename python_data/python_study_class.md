-----------------------------
我们来看一个完整的类，相关的介绍都在注释当中
# We use the "class" statement to create a class
class Human:

    # A class attribute. It is shared by all instances of this class
    # 类属性，可以直接通过Human.species调用，而不需要通过实例
    species = "H. sapiens"

    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by Python but that live in user-controlled
    # namespaces. Methods(or objects or attributes) like: __init__, __str__,
    # __repr__ etc. are called special methods (or sometimes called dunder methods)
    # You should not invent such names on your own.
    # 最基础的构造函数
    # 加了下划线的函数和变量表示不应该被用户使用，其中双下划线的函数或者是变量将不会被子类覆盖
    # 前后都有双下划线的函数和属性是类当中的特殊属性
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

        # Initialize property
        self._age = 0

    # An instance method. All methods take "self" as the first argument
    # 类中的函数，所有实例可以调用，第一个参数必须是self
    # self表示实例的引用
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    # Another instance method
    def sing(self):
        return 'yo... yo... microphone check... one two... one two...'

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    # 加上了注解，表示是类函数
    # 通过Human.get_species来调用，所有实例共享
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    # 静态函数，通过类名或者是实例都可以调用
    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method age() into an read-only attribute of the same name.
    # There's no need to write trivial getters and setters in Python, though.
    @property
    # property注解，类似于get，set方法
    # 效率很低，除非必要，不要使用
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age
复制代码
以上内容的详细介绍之前也有过相关文章，可以查看：
Python——slots，property和对象命名规范
下面我们来看看Python当中类的使用：
# When a Python interpreter reads a source file it executes all its code.
# This __name__ check makes sure this code block is only executed when this
# module is the main program.
# 这个是main函数也是整个程序入口的惯用写法
if __name__ == '__main__':
    # Instantiate a class
    # 实例化一个类，获取类的对象
    i = Human(name="Ian")
    # 执行say方法
    i.say("hi")                     # "Ian: hi"
    j = Human("Joel")
    j.say("hello")                  # "Joel: hello"
    # i和j都是Human的实例，都称作是Human类的对象
    # i and j are instances of type Human, or in other words: they are Human objects

    # Call our class method
    # 类属性被所有实例共享，一旦修改全部生效
    i.say(i.get_species())          # "Ian: H. sapiens"
    # Change the shared attribute
    Human.species = "H. neanderthalensis"
    i.say(i.get_species())          # => "Ian: H. neanderthalensis"
    j.say(j.get_species())          # => "Joel: H. neanderthalensis"

    # 通过类名调用静态方法
    # Call the static method
    print(Human.grunt())            # => "*grunt*"

    # Cannot call static method with instance of object 
    # because i.grunt() will automatically put "self" (the object i) as an argument
    # 不能通过对象调用静态方法，因为对象会传入self实例，会导致不匹配
    print(i.grunt())                # => TypeError: grunt() takes 0 positional arguments but 1 was given

    # Update the property for this instance
    # 实例级别的属性是独立的，各个对象各自拥有，修改不会影响其他对象内的值
    i.age = 42
    # Get the property
    i.say(i.age)                    # => "Ian: 42"
    j.say(j.age)                    # => "Joel: 0"
    # Delete the property
    del i.age
    # i.age                         # => this would raise an AttributeError
复制代码
这里解释一下，实例和对象可以理解成一个概念，实例的英文是instance，对象的英文是object。都是指类经过实例化之后得到的对象。
----------------------------
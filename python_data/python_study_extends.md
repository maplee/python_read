--------------------------
继承可以让子类继承父类的变量以及方法，并且我们还可以在子类当中指定一些属于自己的特性，并且还可以重写父类的一些方法。一般我们会将不同的类放在不同的文件当中，使用import引入，一样可以实现继承。
from human import Human

# Specify the parent class(es) as parameters to the class definition
class Superhero(Human):

    # If the child class should inherit all of the parent's definitions without
    # any modifications, you can just use the "pass" keyword (and nothing else)
    # but in this case it is commented out to allow for a unique child class:
    # pass
    # 如果要完全继承父类的所有的实现，我们可以使用关键字pass，表示跳过。这样不会修改父类当中的实现

    # Child classes can override their parents' attributes
    species = 'Superhuman'

    # Children automatically inherit their parent class's constructor including
    # its arguments, but can also define additional arguments or definitions
    # and override its methods such as the class constructor.
    # This constructor inherits the "name" argument from the "Human" class and
    # adds the "superpower" and "movie" arguments:
    # 子类会完全继承父类的构造方法，我们也可以进行改造，比如额外增加一些参数
    def __init__(self, name, movie=False,
                 superpowers=["super strength", "bulletproofing"]):

        # add additional class attributes:
        # 额外新增的参数
        self.fictional = True
        self.movie = movie
        # be aware of mutable default values, since defaults are shared
        self.superpowers = superpowers

        # The "super" function lets you access the parent class's methods
        # that are overridden by the child, in this case, the __init__ method.
        # This calls the parent class constructor:
        # 子类可以通过super关键字调用父类的方法
        super().__init__(name)

    # override the sing method
    # 重写父类的sing方法
    def sing(self):
        return 'Dun, dun, DUN!'

    # add an additional instance method
    # 新增方法，只属于子类
    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {pow}!".format(pow=power))
复制代码
if __name__ == '__main__':
    sup = Superhero(name="Tick")

    # Instance type checks
    # 检查继承关系
    if isinstance(sup, Human):
        print('I am human')
    # 检查类型
    if type(sup) is Superhero:
        print('I am a superhero')

    # Get the Method Resolution search Order used by both getattr() and super()
    # This attribute is dynamic and can be updated
    # 查看方法查询的顺序
    # 先是自身，然后沿着继承顺序往上，最后到object
    print(Superhero.__mro__)    # => (<class '__main__.Superhero'>,
                                # => <class 'human.Human'>, <class 'object'>)

    # 相同的属性子类覆盖了父类
    # Calls parent method but uses its own class attribute
    print(sup.get_species())    # => Superhuman

    # Calls overridden method
    # 相同的方法也覆盖了父类
    print(sup.sing())           # => Dun, dun, DUN!

    # Calls method from Human
    # 继承了父类的方法
    sup.say('Spoon')            # => Tick: Spoon

    # Call method that exists only in Superhero
    # 子类特有的方法
    sup.boast()                 # => I wield the power of super strength!
                                # => I wield the power of bulletproofing!

    # Inherited class attribute
    sup.age = 31
    print(sup.age)              # => 31

    # Attribute that only exists within Superhero
    print('Am I Oscar eligible? ' + str(sup.movie))
复制代码
---------------------

多继承
--------------------------
我们创建一个蝙蝠类：

# Another class definition
# bat.py
class Bat:

    species = 'Baty'

    def __init__(self, can_fly=True):
        self.fly = can_fly

    # This class also has a say method
    def say(self, msg):
        msg = '... ... ...'
        return msg

    # And its own method as well
    # 蝙蝠独有的声呐方法
    def sonar(self):
        return '))) ... ((('

if __name__ == '__main__':
    b = Bat()
    print(b.say('hello'))
    print(b.fly)
复制代码
我们再创建一个蝙蝠侠的类，同时继承Superhero和Bat：
# And yet another class definition that inherits from Superhero and Bat
# superhero.py
from superhero import Superhero
from bat import Bat

# Define Batman as a child that inherits from both Superhero and Bat
class Batman(Superhero, Bat):

    def __init__(self, *args, **kwargs):
        # Typically to inherit attributes you have to call super:
        # super(Batman, self).__init__(*args, **kwargs)      
        # However we are dealing with multiple inheritance here, and super()
        # only works with the next base class in the MRO list.
        # So instead we explicitly call __init__ for all ancestors.
        # The use of *args and **kwargs allows for a clean way to pass arguments,
        # with each parent "peeling a layer of the onion".
        # 通过类名调用两个父类各自的构造方法
        Superhero.__init__(self, 'anonymous', movie=True, 
                           superpowers=['Wealthy'], *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        # override the value for the name attribute
        self.name = 'Sad Affleck'

    # 重写父类的sing方法
    def sing(self):
        return 'nan nan nan nan nan batman!'
复制代码
执行这个类：
if __name__ == '__main__':
    sup = Batman()

    # Get the Method Resolution search Order used by both getattr() and super().
    # This attribute is dynamic and can be updated
    # 可以看到方法查询的顺序是先沿着superhero这条线到human，然后才是bat
    print(Batman.__mro__)       # => (<class '__main__.Batman'>, 
                                # => <class 'superhero.Superhero'>, 
                                # => <class 'human.Human'>, 
                                # => <class 'bat.Bat'>, <class 'object'>)

    # Calls parent method but uses its own class attribute
    # 只有superhero有get_species方法
    print(sup.get_species())    # => Superhuman

    # Calls overridden method
    print(sup.sing())           # => nan nan nan nan nan batman!

    # Calls method from Human, because inheritance order matters
    sup.say('I agree')          # => Sad Affleck: I agree

    # Call method that exists only in 2nd ancestor
    # 调用蝙蝠类的声呐方法
    print(sup.sonar())          # => ))) ... (((

    # Inherited class attribute
    sup.age = 100
    print(sup.age)              # => 100

    # Inherited attribute from 2nd ancestor whose default value was overridden.
    print('Can I fly? ' + str(sup.fly)) # => Can I fly? False
-------------------------
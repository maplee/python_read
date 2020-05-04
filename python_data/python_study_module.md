-------------------------
使用import语句引入一个Python模块，我们可以用.来访问模块中的函数或者是类。
# You can import modules
import math
print(math.sqrt(16))  # => 4.0
复制代码
我们也可以使用from import的语句，单独引入模块内的函数或者是类，而不再需要写出完整路径。使用from import *可以引入模块内所有内容（不推荐这么干）
# You can get specific functions from a module
from math import ceil, floor
print(ceil(3.7))   # => 4.0
print(floor(3.7))  # => 3.0
# You can import all functions from a module.
# Warning: this is not recommended
from math import *
复制代码
可以使用as给模块内的方法或者类起别名：
# You can shorten module names
import math as m
math.sqrt(16) == m.sqrt(16)  # => True
复制代码
我们可以使用dir查看我们用的模块的路径：
# You can find out which functions and attributes
# are defined in a module.
import math
dir(math)
复制代码
这么做的原因是如果我们当前的路径下也有一个叫做math的Python文件，那么会覆盖系统自带的math的模块。这是尤其需要注意的，不小心会导致很多奇怪的bug。
----------------------
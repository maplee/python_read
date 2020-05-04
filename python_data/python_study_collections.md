list
------------------
Python中用[]表示空的list，我们也可以直接在其中填充元素进行初始化：
# Lists store sequences
li = []
# You can start with a prefilled list
other_li = [4, 5, 6]
复制代码
使用append和pop可以在list的末尾插入或者删除元素：
# Add stuff to the end of a list with append
li.append(1)    # li is now [1]
li.append(2)    # li is now [1, 2]
li.append(4)    # li is now [1, 2, 4]
li.append(3)    # li is now [1, 2, 4, 3]
# Remove from the end with pop
li.pop()        # => 3 and li is now [1, 2, 4]
# Let's put it back
li.append(3)    # li is now [1, 2, 4, 3] again.
复制代码
list可以通过[]加上下标访问指定位置的元素，如果是负数，则表示倒序访问。-1表示最后一个元素，-2表示倒数第二个，以此类推。如果访问的元素超过数组长度，则会出发IndexError的错误。
# Access a list like you would any array
li[0]   # => 1
# Look at the last element
li[-1]  # => 3

# Looking out of bounds is an IndexError
li[4]  # Raises an IndexError
复制代码
list支持切片操作，所谓的切片则是从原list当中拷贝出指定的一段。我们用start: end的格式来获取切片，注意，这是一个左闭右开区间。如果留空表示全部获取，我们也可以额外再加入一个参数表示步长，比如[1:5:2]表示从1号位置开始，步长为2获取元素。得到的结果为[1, 3]。如果步长设置成-1则代表反向遍历。
# You can look at ranges with slice syntax.
# The start index is included, the end index is not
# (It's a closed/open range for you mathy types.)
li[1:3]   # Return list from index 1 to 3 => [2, 4]
li[2:]    # Return list starting from index 2 => [4, 3]
li[:3]    # Return list from beginning until index 3  => [1, 2, 4]
li[::2]   # Return list selecting every second entry => [1, 4]
li[::-1]  # Return list in reverse order => [3, 4, 2, 1]
# Use any combination of these to make advanced slices
# li[start:end:step]
复制代码
如果我们要指定一段区间倒序，则前面的start和end也需要反过来，例如我想要获取[3: 6]区间的倒序，应该写成[6:3:-1]。
只写一个:，表示全部拷贝，如果用is判断拷贝前后的list会得到False。可以使用del删除指定位置的元素，或者可以使用remove方法。
# Make a one layer deep copy using slices
li2 = li[:]  # => li2 = [1, 2, 4, 3] but (li2 is li) will result in false.

# Remove arbitrary elements from a list with "del"
del li[2]  # li is now [1, 2, 3]

# Remove first occurrence of a value
li.remove(2)  # li is now [1, 3]
li.remove(2)  # Raises a ValueError as 2 is not in the list
复制代码
insert方法可以指定位置插入元素，index方法可以查询某个元素第一次出现的下标。
# Insert an element at a specific index
li.insert(1, 2)  # li is now [1, 2, 3] again

# Get the index of the first item found matching the argument
li.index(2)  # => 1
li.index(4)  # Raises a ValueError as 4 is not in the list
复制代码
list可以进行加法运算，两个list相加表示list当中的元素合并。等价于使用extend方法：
# You can add lists
# Note: values for li and for other_li are not modified.
li + other_li  # => [1, 2, 3, 4, 5, 6]

# Concatenate lists with "extend()"
li.extend(other_li)  # Now li is [1, 2, 3, 4, 5, 6]
复制代码
我们想要判断元素是否在list中出现，可以使用in关键字，通过使用len计算list的长度：
# Check for existence in a list with "in"
1 in li  # => True

# Examine the length with "len()"
len(li)  # => 6
复制代码
---------------
tuple
-----------------
tuple和list非常接近，tuple通过()初始化。和list不同，tuple是不可变对象。也就是说tuple一旦生成不可以改变。如果我们修改tuple，会引发TypeError异常。
# Tuples are like lists but are immutable.
tup = (1, 2, 3)
tup[0]      # => 1
tup[0] = 3  # Raises a TypeError
复制代码
由于小括号是有改变优先级的含义，所以我们定义单个元素的tuple，末尾必须加上逗号，否则会被当成是单个元素：
# Note that a tuple of length one has to have a comma after the last element but
# tuples of other lengths, even zero, do not.
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>
复制代码
tuple支持list当中绝大部分操作：
# You can do most of the list operations on tuples too
len(tup)         # => 3
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tup[:2]          # => (1, 2)
2 in tup         # => True
复制代码
我们可以用多个变量来解压一个tuple：
# You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
# You can also do extended unpacking
a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4
# Tuples are created by default if you leave out the parentheses
d, e, f = 4, 5, 6  # tuple 4, 5, 6 is unpacked into variables d, e and f
# respectively such that d = 4, e = 5 and f = 6
# Now look how easy it is to swap two values
e, d = d, e  # d is now 5 and e is now 4
复制代码
解释一下这行代码：
a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4
复制代码
我们在b的前面加上了星号，表示这是一个list。所以Python会在将其他变量对应上值的情况下，将剩下的元素都赋值给b。
补充一点，tuple本身虽然是不可变的，但是tuple当中的可变元素是可以改变的。比如我们有这样一个tuple：
a = (3, [4])
复制代码
我们虽然不能往a当中添加或者删除元素，但是a当中含有一个list，我们可以改变这个list类型的元素，这并不会触发tuple的异常：
a[1].append(0) # 这是合法的
复制代码
------------------
dict
------------------
dict也是Python当中经常使用的容器，它等价于C++当中的map，即存储key和value的键值对。我们用{}表示一个dict，用:分隔key和value。
# Dictionaries store mappings from keys to values
empty_dict = {}
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}
复制代码
dict的key必须为不可变对象，所以list、set和dict不可以作为另一个dict的key，否则会抛出异常：
# Note keys for dictionaries have to be immutable types. This is to ensure that
# the key can be converted to a constant hash value for quick look-ups.
# Immutable types include ints, floats, strings, tuples.
invalid_dict = {[1,2,3]: "123"}  # => Raises a TypeError: unhashable type: 'list'
valid_dict = {(1,2,3):[1,2,3]}   # Values can be of any type, however.
复制代码
我们同样用[]查找dict当中的元素，我们传入key，获得value，等价于get方法。
# Look up values with []
filled_dict["one"]  # => 1
filled_dict.get('one') #=> 1
复制代码
我们可以call dict当中的keys和values方法，获取dict当中的所有key和value的集合，会得到一个list。在Python3.7以下版本当中，返回的结果的顺序可能和插入顺序不同，在Python3.7及以上版本中，Python会保证返回的顺序和插入顺序一致：
# Get all keys as an iterable with "keys()". We need to wrap the call in list()
# to turn it into a list. We'll talk about those later.  Note - for Python
# versions <3.7, dictionary key ordering is not guaranteed. Your results might
# not match the example below exactly. However, as of Python 3.7, dictionary
# items maintain the order at which they are inserted into the dictionary.
list(filled_dict.keys())  # => ["three", "two", "one"] in Python <3.7
list(filled_dict.keys())  # => ["one", "two", "three"] in Python 3.7+

# Get all values as an iterable with "values()". Once again we need to wrap it
# in list() to get it out of the iterable. Note - Same as above regarding key
# ordering.
list(filled_dict.values())  # => [3, 2, 1]  in Python <3.7
list(filled_dict.values())  # => [1, 2, 3] in Python 3.7+
复制代码
我们也可以用in判断一个key是否在dict当中，注意只能判断key。
# Check for existence of keys in a dictionary with "in"
"one" in filled_dict  # => True
1 in filled_dict      # => False
复制代码
如果使用[]查找不存在的key，会引发KeyError的异常。如果使用get方法则不会引起异常，只会得到一个None：
# Looking up a non-existing key is a KeyError
filled_dict["four"]  # KeyError

# Use "get()" method to avoid the KeyError
filled_dict.get("one")      # => 1
filled_dict.get("four")     # => None
# The get method supports a default argument when the value is missing
filled_dict.get("one", 4)   # => 1
filled_dict.get("four", 4)  # => 4
复制代码
setdefault方法可以为不存在的key插入一个value，如果key已经存在，则不会覆盖它：
# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5
复制代码
我们可以使用update方法用另外一个dict来更新当前dict，比如a.update(b)。对于a和b交集的key会被b覆盖，a当中不存在的key会被插入进来：
# Adding to a dictionary
filled_dict.update({"four":4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4         # another way to add to dict
复制代码
我们一样可以使用del删除dict当中的元素，同样只能传入key。
Python3.5以上的版本支持使用**来解压一个dict：
{'a': 1, **{'b': 2}}  # => {'a': 1, 'b': 2}
{'a': 1, **{'a': 2}}  # => {'a': 2}
复制代码
------------------
set
------------------
set是用来存储不重复元素的容器，当中的元素都是不同的，相同的元素会被删除。我们可以通过set()，或者通过{}来进行初始化。注意当我们使用{}的时候，必须要传入数据，否则Python会将它和dict弄混。
# Sets store ... well sets
empty_set = set()
# Initialize a set with a bunch of values. Yeah, it looks a bit like a dict. Sorry.
some_set = {1, 1, 2, 2, 3, 4}  # some_set is now {1, 2, 3, 4}
复制代码
set当中的元素也必须是不可变对象，因此list不能传入set。
# Similar to keys of a dictionary, elements of a set have to be immutable.
invalid_set = {[1], 1}  # => Raises a TypeError: unhashable type: 'list'
valid_set = {(1,), 1}
复制代码
可以调用add方法为set插入元素：
# Add one more item to the set
filled_set = some_set
filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}
# Sets do not have duplicate elements
filled_set.add(5)  # it remains as before {1, 2, 3, 4, 5}
复制代码
set还可以被认为是集合，所以它还支持一些集合交叉并补的操作。
# Do set intersection with &
# 计算交集
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}

# Do set union with |
# 计算并集
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}

# Do set difference with -
# 计算差集
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}

# Do set symmetric difference with ^
# 这个有点特殊，计算对称集，也就是去掉重复元素剩下的内容
{1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}
复制代码
set还支持超集和子集的判断，我们可以用大于等于和小于等于号判断一个set是不是另一个的超集或子集：
# Check if set on the left is a superset of set on the right
{1, 2} >= {1, 2, 3} # => False

# Check if set on the left is a subset of set on the right
{1, 2} <= {1, 2, 3} # => True
复制代码
和dict一样，我们可以使用in判断元素在不在set当中。用copy可以拷贝一个set。
# Check for existence in a set with in
2 in filled_set   # => True
10 in filled_set  # => False

# Make a one layer deep copy
filled_set = some_set.copy()  # filled_set is {1, 2, 3, 4, 5}
filled_set is some_set        # => False
------------------------------
变量
------------
Python中声明对象不需要带上类型，直接赋值即可，Python会自动关联类型，如果我们使用之前没有声明过的变量则会出发NameError异常。
# There are no declarations, only assignments.
# Convention is to use lower_case_with_underscores
some_var = 5
some_var  # => 5

# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
some_unknown_var  # Raises a NameError
复制代码
Python支持三元表达式，但是语法和C++不同，使用if else结构，写成：
# if can be used as an expression
# Equivalent of C's '?:' ternary operator
"yahoo!" if 3 > 2 else 2  # => "yahoo!"
复制代码
上段代码等价于：
if 3 > 2:
    return 'yahoo'
else:
    return 2
------------
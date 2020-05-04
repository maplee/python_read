输入输出
--------------
Python当中的标准输入输出是input和print。
print会输出一个字符串，如果传入的不是字符串会自动调用__str__方法转成字符串进行输出。默认输出会自动换行，如果想要以不同的字符结尾代替换行，可以传入end参数：
# Python has a print function
print("I'm Python. Nice to meet you!")  # => I'm Python. Nice to meet you!

# By default the print function also prints out a newline at the end.
# Use the optional argument end to change the end string.
print("Hello, World", end="!")  # => Hello, World!
复制代码
使用input时，Python会在命令行接收一行字符串作为输入。可以在input当中传入字符串，会被当成提示输出：
# Simple way to get input data from console
input_string_var = input("Enter some data: ") # Returns the data as a string
# Note: In earlier versions of Python, input() method was named as raw_input()
-------------
#!/usr/bin/python
# coding=utf-8

import sys
import csv
import math



#基础变量类型与操作符
def fun_stanard():
	print("[1.1].逻辑运算\r\n")
	text  = '\tPython当中的数字定义和其他语言一样：# 获得一个浮点数 10.0\r\n\r\n'

	text  = text+'\t我们分别使用+, -, *, /表示加减乘除四则运算符。：1 + 1   # => 2 \r\n\r\n'

	text  = text+'\t这里要注意的是，在Python2当中，10/3这个操作会得到3，而不是3.33333。因为除数和被除数都是整数，所以Python会自动执行整数的计算，帮我们把得到的商取整。如果是10.0 / 3，就会得到3.33333。目前Python2已经不再维护了，可以不用关心其中的细节。但问题是Python是一个弱类型的语言，如果我们在一个函数当中得到两个变量，是无法直接判断它们的类型的。这就导致了同样的计算符可能会得到不同的结果，这非常蛋疼。以至于程序员在运算除法的时候，往往都需要手工加上类型转化符，将被除数转成浮点数。在Python3当中拨乱反正，修正了这个问题，即使是两个整数相除，并且可以整除的情况下，得到的结果也一定是浮点数。如果我们想要得到整数，我们可以这么操作：5//3  # => 1 \r\n\r\n'
	
	text  = text+'\t两个除号表示取整除，Python会为我们保留去除余数的结果。除了取整除操作之外还有取余数操作，数学上称为取模，Python中用%表示：7 % 3  # => 1 \r\n\r\n'
	
	text  = text+'\tPython中支持乘方运算，我们可以不用调用额外的函数，而使用**符号来完成：2**3  # => 8\r\n\r\n'

	text  = text+'\t当运算比较复杂的时候，我们可以用括号来强制改变运算顺序。：(1 + 3) * 2  # => 8")\r\n\r\n'
	print(text)

	print("[1.2].list和字符串\r\n")
	text  = '\t关于list的判断，我们常用的判断有两种，一种是刚才介绍的==，还有一种是is。我们有时候也会简单实用is来判断，那么这两者有什么区别呢？我们来看下面的例子\r\n\r\n'

	text  = text +'\t\ta = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]\r\n'
	text  = text +'\t\tb = a             # Point b at what a is pointing to\r\n'
	text  = text +'\t\tb is a            # => True, a and b refer to the same object\r\n'
	text  = text +'\t\tb == a            # => True, a\'s and b\'s objects are equal\r\n'
	text  = text +'\t\tb = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]\r\n'
	text  = text +'\t\tb is a            # => False, a and b do not refer to the same object\r\n'
	text  = text +'\t\tb == a            # => True, a\'s and b\'s objects are equal\r\n\r\n'

	text  = text+'\tPython是全引用的语言，其中的对象都使用引用来表示。is判断的就是两个引用是否指向同一个对象，而==则是判断两个引用指向的具体内容是否相等。举个例子，如果我们把引用比喻成地址的话，is就是判断两个变量的是否指向同一个地址，比如说都是沿河东路XX号。而==则是判断这两个地址的收件人是否都叫张三。\r\n'
	text  = text +'\t显然，住在同一个地址的人一定都叫张三，但是住在不同地址的两个人也可以都叫张三，也可以叫不同的名字。所以如果a is b，那么a == b一定成立，反之则不然。\r\n'
	text  = text +'\tPython当中对字符串的限制比较松，双引号和单引号都可以表示字符串，看个人喜好使用单引号或者是双引号。我个人比较喜欢单引号，因为写起来方便。\r\n'
	text  = text +'\t字符串也支持+操作，表示两个字符串相连。除此之外，我们把两个字符串写在一起，即使没有+，Python也会为我们拼接：\r\n\r\n'
	text = text+'\t\t# Strings are created with \"  \r\n'
	text  = text +'\t\t\"This is a string.\"\r\n'
	text  = text +'\t\t\'This is also a string.\'\r\n'
	text  = text +'\t\t# Strings can be added too! But try not to do this.\r\n'
	text  = text +'\t\t\"Hello \" + \"world!\"  # => \"Hello world!\"\r\n'
	text  = text +'\t\t# String literals (but not variables) can be concatenated without using \r\n'
	text  = text +'\t\t\"Hello \" \"world!\"    # => \"Hello world!\" \r\n\r\n'

	text  = text+'\t我们可以使用[]来查找字符串当中某个位置的字符，用len来计算字符串的长度。")\r\n'
	text = text +'# A string can be treated like a list of characters \r\n'
	text  = text +'\t\t\"This is a string\"[0]  # => \'T\' \r\n'
	text  = text +'\t\t# You can find the length of a string \r\n'
	text  = text +'\t\tlen(\"This is a string\")  # => 16\r\n\r\n'

	text = text + '我们可以在字符串前面加上f表示格式操作，并且在格式操作当中也支持运算，比如可以嵌套上len函数等。不过要注意，只有Python3.6以上的版本支持f操作。\r\n\r\n'

	text = text + '\t\t# You can also format using f-strings or formatted string literals (in Python 3.6+) \r\n'
	text = text + '\t\tname = \"Reiko\" \r\n'
	text = text + '\t\tf\"She said her name is {name}.\" # => \"She said her name is Reiko\" \r\n'
	text = text + '\t\t# You can basically put any Python statement inside the braces and it will be output in the string. \r\n'
	text = text + '\t\tf\"{name} is {len(name)} characters long.\" # => \"Reiko is 5 characters long.\"\r\n\r\n'

	# text = text + 

	print(text)
	main_menu()
	

#读取文件
def fun_read_file(file):
	# Read the entire file as a single string
	# with open(file, 'rt',encoding='utf-8') as f:
	# 	data = f.read()
	# 	f.close()
	data =''
	# Iterate over the lines of the file
	with open(file, 'rt',encoding='utf-8') as f:
		for line in f:
			# process line
			data = data + '\t\t'+line + '\r\n'
	f.close()
	return data

#输入输出
def fun_input_print():
	# Read the entire file as a single string
	file = 'python_data/python_study_input_print.md'
	print(fun_read_file(file))


#变量与集合
def fun_list_str():
	print("[2].变量与集合")
	fun_input_print()
	file = 'python_data/python_study_variate.md'
	print(fun_read_file(file))
	file = 'python_data/python_study_collections.md'
	print(fun_read_file(file))
	main_menu()

#控制流和迭代
def fun_Control_flow_iteration():
	print("\t[3].控制流和迭代")
	file = 'python_data/python_study_Control_flow_iteration.md'
	print(fun_read_file(file))
	main_menu()





#模块
def fun_module():
	print("\t[4].模块")
	file = 'python_data/python_study_module.md'
	print(fun_read_file(file))
	main_menu()



#类
def fun_class():
	print("\t[5].类")
	file = 'python_data/python_study_class.md'
	print(fun_read_file(file))
	main_menu()


#继承
def fun_extends():
	print("\t[6].继承")
	file = 'python_data/python_study_extends.md'
	print(fun_read_file(file))
	main_menu()


#进阶
def fun_advance():
	print("\t[7].进阶")
	file = 'python_data/python_study_advance.md'
	print(fun_read_file(file))
	main_menu()

def main_menu():
	print("Python功能：")
	print("[1].基础变量类型与操作符")
	print("[2].变量与集合")
	print("[3].控制流和迭代")
	print("[4].模块")
	print("[5].类")
	print("[6].继承")
	print("[7].进阶")
	print("[0].退出")
	inputStr = input("请选择您要学习的功能序号\r\n")
	num = int(inputStr,base=0)
	if(num < 0 or num >7):
		inputStr = input("输入有误，请选择您要学习的功能序号\r\n")
		num = int(inputStr,base=0)
	#功能选择
	if(num >= 0 and num <= 7):
		if(num == 1):
			try:
				sys.exit(0)
			except:
				print('Program is dead.')

		if(num == 1):
			fun_stanard()
		if(num == 2):
			fun_list_str()
		if(num == 3):
			fun_Control_flow_iteration()
		if(num == 4):
			fun_module()
		if(num == 5):
			fun_class()
		if(num == 6):
			fun_extends()
		if(num == 7):
			fun_advance()							



main_menu()
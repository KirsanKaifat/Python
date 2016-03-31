print("Calculator 1.2\nYou can use +,-,*,/\nEnter 'clear' for starting new caclulation\nEnter 'x' for exit")

def input_num():
	while True:
		result = input()
		if result == "x":
			exit()
		try:
			num = float(result)
			break
		except ValueError:
			print("Incorrect number")
	return num
		
def use_operation():
	global num
	while True:	
		std_in_op = input()
		if std_in_op == "x":
			exit()
		if std_in_op == "clear":
			num = input_num()
			continue
		if std_in_op == "+":
			num += input_num()
			break
		elif std_in_op == "-":
			num -= input_num()
			break
		elif std_in_op == "*":
			num *= input_num()
			break
		elif std_in_op == "/":
			num /= input_num()
			break
		else:
			print("Incorrect operation")

num = input_num()
while True:
	use_operation()
	print("=" , num)
		

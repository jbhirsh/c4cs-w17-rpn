#!/usr/bin/env python3

import operator
import readline

import sys
from termcolor import colored, cprint

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'%': operator.mod,
	'//': operator.floordiv,
}

def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
	return stack.pop()

def main():
	text = colored('Hi, welcome to my calculator!', 'magenta', attrs=['bold','blink'])
	print(text)
	while True:
		result = calculate(input('rpn calc> '))
		if result < 0:
			cprint("Result:", result, 'red')
		else:
			cprint("Result:", result, 'green')

if __name__ == '__main__':
	main()

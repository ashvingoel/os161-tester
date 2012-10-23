#!/usr/bin/python

import core
import sys

def testCrash(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing crash")
	#Please check this and the correct value
	check = 'Fatal user mode trap'
	commands = 'a b c d e g h i j k l m n o'
	for i in commands:
		test.send_command("p /testbin/crash " + i)
		test.look_for_and_print_result(check, 5)

	test.clean_kernel()

def main():
	path = str(sys.argv[1])
	testCrash(path)



if __name__ == "__main__":
	main()

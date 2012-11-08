#!/usr/bin/python

import core
import sys

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing fork")
	#check = '00aa111b1bbb2222c22c2cc2cccc'
	check = '00aa1111bbbb222222c2ccc2cccc'
	test.send_command("p /testbin/fork")
	test.look_for_and_print_result(check, 8)

def main():
	path = str(sys.argv[1])
	testPrintChar(path)



if __name__ == "__main__":
	main()

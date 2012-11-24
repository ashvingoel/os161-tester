#!/usr/bin/python

import core
import sys

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing matmult")
	test.set_timeout(60)
	check1 = 'answer is'
	check2 = '8772192'
	check3 = 'should be 8772192'
	test.send_command("p /testbin/matmult")
	ret = test.look_for(check1)
	if ret >= 0:
		ret = test.look_for(check2)
		if ret >= 0:
			test.look_for_and_print_result(check3, 5)
		else:
			test.print_result(0, 5)
	else:
		test.print_result(0,5)

def main():
	path = str(sys.argv[1])
	testPrintChar(path)


if __name__ == "__main__":
	main()

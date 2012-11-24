#!/usr/bin/python

import core
import sys

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing matmult")
	test.set_timeout(60)
	check = 'answer is: 8772192\(should be 8772192\)'
	test.send_command("p /testbin/matmult")
	test.look_for_and_print_result(check, 5)

def main():
	path = str(sys.argv[1])
	testPrintChar(path)


if __name__ == "__main__":
	main()

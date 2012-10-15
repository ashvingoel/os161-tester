#!/usr/bin/python

import core
import sys

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing add")
	check = 'Answer: 5'
	test.send_command("p /testbin/add 2 3")
	test.look_for_and_print_result(check)

def main():
	path = str(sys.argv[1])
	testPrintChar(path)



if __name__ == "__main__":
	main()

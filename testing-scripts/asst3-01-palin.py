#!/usr/bin/python

import core
import sys

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "palin")
	test.runprogram("/testbin/palin")
	check = 'IS a palindrome'
	test.look_for_and_print_result(check, 4)

def main():
	path = str(sys.argv[1])
	testPrintChar(path)


if __name__ == "__main__":
	main()

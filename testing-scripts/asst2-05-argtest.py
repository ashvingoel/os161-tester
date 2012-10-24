#!/usr/bin/python

import core
import sys

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing arg")
	check1 = 'argc: 2'
	check2 = 'argv\[0\]: \/testbin\/argtest'
	check3 = 'argv\[1\]: test'
	test.send_command("p /testbin/argtest test")
	test.look_for_and_print_result(check1, 4)
	test.look_for_and_print_result(check2, 4)
	test.look_for_and_print_result(check3, 4)

def main():
	path = str(sys.argv[1])
	testPrintChar(path)



if __name__ == "__main__":
	main()

#!/usr/bin/python

import core
import sys
import pexpect

def testCrash(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing crash")
	#Please check this and the correct value
	check = 'Fatal user mode trap'
	commands = 'abcdeghijklmno'
	for i in commands:
		res = test.send_command("p /testbin/crash " + i)
		if res is not True:
			test.set_failure(70, 5)
			break
		test.look_for_and_print_result(check, 5)
		if test.look_for(pexpect.EOF >= 0):
			continue

	test.clean_kernel()

def main():
	path = str(sys.argv[1])
	testCrash(path)



if __name__ == "__main__":
	main()

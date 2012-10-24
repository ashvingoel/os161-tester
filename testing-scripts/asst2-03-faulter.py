#!/usr/bin/python

import core
import sys

def testFaulter(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing faulter")
	check = 'Entering the faulter program - I should die immediately'
	test.send_command("p /testbin/faulter")
	test.look_for_and_print_result(check, 5)
	if test.send_command("p /testbin/faulter") is not True:
		test.set_failure(5, 5)
	test.clean_kernel()

def main():
	path = str(sys.argv[1])
	testFaulter(path)



if __name__ == "__main__":
	main()

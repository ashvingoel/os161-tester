#!/usr/bin/python

import core
import sys

def testFaulter(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing faulter")
	check = 'Entering the faulter program - I should die immediately'
	test.runprogram("/testbin/faulter")
	test.look_for_and_print_result(check, 8)

def main():
	path = str(sys.argv[1])
	testFaulter(path)



if __name__ == "__main__":
	main()

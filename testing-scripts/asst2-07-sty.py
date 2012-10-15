#!/usr/bin/python

import core
import sys

def testSty(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing forktest")
	#Please check this and the correct value
	check = ''
	test.send_command("p /testbin/sty")
	test.look_for_and_print_result(check)

def main():
	path = str(sys.argv[1])
	testSty(path)



if __name__ == "__main__":
	main()

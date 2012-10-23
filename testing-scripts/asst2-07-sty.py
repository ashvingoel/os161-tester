#!/usr/bin/python

import core
import sys

def testSty(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing forktest")
	#This is bogus, need to come up with somethign better
	check = 'OS\/161 kernel \[\? for menu\]\: '
	test.send_command("p /testbin/sty")
	test.look_for_and_print_result(check, 5)
	test.clean_kernel()

def main():
	path = str(sys.argv[1])
	testSty(path)



if __name__ == "__main__":
	main()

#!/usr/bin/python

import core
import sys
import re

def testPrintChar(kernel_name):
	global test
        out = 0
	test = core.TestUnit(kernel_name, "sty")
        check = '\nOperation took.* seconds'
	for i in range(10):
            test.runprogram("/testbin/sty")
            out = test.look_for(check)
            if out < 0:
                break
	if out >= 0:
		test.print_result(10, 10)
	else:
		test.print_result(0, 10)

def main():
	path = str(sys.argv[1])
	testPrintChar(path)



if __name__ == "__main__":
	main()

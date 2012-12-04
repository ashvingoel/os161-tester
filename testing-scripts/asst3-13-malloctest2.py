#!/usr/bin/python

import core
import sys

def test(kernel_name):
	test = core.TestUnit(kernel_name, "malloctest 2")
        test.runprogram("/testbin/malloctest", "2")
	test.set_timeout(300)
        test.look_for_and_print_result('\nPassed malloc test 2.', 10)

def main():
	path = str(sys.argv[1])
	test(path)

if __name__ == "__main__":
	main()

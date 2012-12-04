#!/usr/bin/python

import core
import sys

def test(kernel_name):
	test = core.TestUnit(kernel_name, "malloctest 5")
        test.runprogram("/testbin/malloctest", "5")
	test.set_timeout(40)
        test.look_for_and_print_result('\nPassed malloc test 5.', 10)

def main():
	path = str(sys.argv[1])
	test(path)

if __name__ == "__main__":
	main()

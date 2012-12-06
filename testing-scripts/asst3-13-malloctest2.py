#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("malloctest 2")
    test.runprogram("/testbin/malloctest", "2")
    test.set_timeout(300)
    test.look_for_and_print_result('\nPassed malloc test 2.', 10)

if __name__ == "__main__":
	main()

#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("malloctest 1")
    test.runprogram("/testbin/malloctest", "1")
    test.look_for_and_print_result('\nPassed malloc test 1.', 5)

if __name__ == "__main__":
	main()

#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("malloctest 5")
    test.runprogram("/testbin/malloctest", "5")
    test.set_timeout(40)
    test.look_for_and_print_result('\nPassed malloc test 5.', 10)

if __name__ == "__main__":
	main()

#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("argtest")
    test.runprogram("/testbin/argtest", "test")
    check1 = 'argc: 2'
    # check2 = 'argv\[0\]: '+ "/testbin/argtest"
    check2 = 'argv\[0\]: '+ "/testbin/os161testerprog"
    check3 = 'argv\[1\]: test'
    test.look_for_and_print_result_no_wait(check1, 2)
    test.look_for_and_print_result_no_wait(check2, 3)
    test.look_for_and_print_result(check3, 3)

if __name__ == "__main__":
	main()

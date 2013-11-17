#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("printf")
    test.runprogram("/testbin/printf")
    check = 'printf works\!'
    # parent is not synchronized with child, so don't wait for menu
    test.look_for_and_print_result_no_wait(check, 12)

if __name__ == "__main__":
    main()

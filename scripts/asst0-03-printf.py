#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("printf")
    test.runprogram("/testbin/printf")
    check = 'printf works\!'
    test.look_for_and_print_result(check, 12)

if __name__ == "__main__":
    main()

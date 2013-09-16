#!/usr/bin/python

import core
import sys
import re

def main():
    out = 0
    test = core.TestUnit("sty")
    check = '\nOperation took.* seconds'
    for i in range(10):
        # TODO: should we check that we built sty
        test.runprogram("/testbin/sty")
        out = test.look_for(check)
        if out < 0:
            break
    if out >= 0:
        test.print_result(10, 10)
    else:
        test.print_result(0, 10)

if __name__ == "__main__":
    main()

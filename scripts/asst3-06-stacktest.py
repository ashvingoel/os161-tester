#!/usr/bin/python

import core
import sys
import os

def main():
    out = 0
    test = core.TestUnit("stacktest")
    test.runprogram("/testbin/stacktest")
    for i in range(4000):
        check = "\ncalling foo: n-i = " + str(i)
        out = test.look_for(check)
        if out < 0:
            break
    if out >= 0:
        test.print_result(5, 5)
    else:
        test.print_result(0, 5)

if __name__ == "__main__":
	main()

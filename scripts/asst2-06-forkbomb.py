#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("forkbomb")
    check = 'OS\/161 kernel \[\? for menu\]\: '
    test.runprogram("/testbin/forkbomb")
    result = test.look_for(check)

    if result != -1:
        test.print_result(0, 8)
    else:
        test.print_result(8, 8)

if __name__ == "__main__":
	main()

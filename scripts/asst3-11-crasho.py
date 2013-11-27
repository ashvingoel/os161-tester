#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("crasho")
    test.runprogram("/testbin/crash", "o")
    test.set_timeout(540)
    test.look_for_and_print_result('\nFatal user mode trap (3|4)', 10)

if __name__ == "__main__":
	main()

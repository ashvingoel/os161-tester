#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("matmult")
    test.runprogram("/testbin/matmult")
    test.set_timeout(60)
    test.look_for_and_print_result('\nPassed.', 10)

if __name__ == "__main__":
	main()

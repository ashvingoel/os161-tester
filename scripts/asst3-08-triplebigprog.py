#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("triplebigprog")
    test.runprogram("/testbin/triplebigprog")
    # runprogram changes the name of the program
    test.look_for_and_print_result(': Congratulations! You passed.', 20)

if __name__ == "__main__":
	main()

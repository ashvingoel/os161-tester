#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("triplemat")
    test.runprogram("/testbin/triplemat")
    test.set_timeout(720)
    # runprogram changes the name of the program
    test.look_for_and_print_result(': Congratulations! You passed.', 20)

if __name__ == "__main__":
	main()

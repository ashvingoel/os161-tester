#!/usr/bin/python

import core
import sys
import pexpect



def testCrash(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing crash")
	#Please check this and the correct value
	check = 'Fatal user mode trap '
        outputs = {'a' : 2, 'b' : 2, 'c' : 4, 'd' : 3, 'e' : 3, \
                       'g' : 5, 'h' : 2, 'i' : 2, 'j' : 4, 'k' : 4, \
                       'l' : 10, 'm' : 9, 'n' : 9, 'o' : 3}

        keylist = outputs.keys()
        keylist.sort()
	for i in keylist:
            res = test.runprogram("/testbin/crash")
            test.look_for("Choose:")
            # the second argument is 0, so don't wait for menu prompt
            res = test.send_command(i, 0)
            test.look_for_and_print_result(check + str(outputs[i]), 1)

def main():
	path = str(sys.argv[1])
	testCrash(path)



if __name__ == "__main__":
	main()

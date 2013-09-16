#!/usr/bin/python

import core
import sys

def main():
	test = core.TestUnit("fork")
        test.runprogram("/testbin/fork")
	out = test.look_for("([0a1b2]{20,20})$")
	if out < 0:
		test.print_result(0, 8)
                return

        output = test.kernel.match.group(0)
        output_array = {'0' : 0, 'a': 0, '1' : 0, 'b' : 0, '2':0}
        for i in range(len(output)):
            index = output[i]
            output_array[index] += 1
        if (output_array['0'] == 2) and \
                (output_array['a'] == 2) and \
                (output_array['1'] == 4) and \
                (output_array['b'] == 4) and \
                (output_array['2'] == 8):
            test.print_result(8,8)
        else:
            print "Output didn't match"
            test.print_result(0,8)

if __name__ == "__main__":
	main()

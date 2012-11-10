#!/usr/bin/python

import core
import sys

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing fork")
	#check = '00aa111b1bbb2222c22c2cc2cccc'
	#check = '00aa1111bbbb222222c2ccc2cccc'
	#check = '00aa1111bbbb22222222'
	test.send_command("p /testbin/fork")
	out = test.look_for("([0a1b2]{20,20})$")
	if out < 0:
		test.print_result(0, 8)
	else:
		output = test.kernel.match.group(0)
		output_array['0'] = 0
		output_array['a'] = 0
		output_array['1'] = 0
		output_array['b'] = 0
		output_array['2'] = 0
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

def main():
	path = str(sys.argv[1])
	testPrintChar(path)



if __name__ == "__main__":
	main()

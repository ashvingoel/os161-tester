
#!/usr/bin/python

import core
import sys

def testForkBomb(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing forkbomb")
	#Please check this and the correct value
	check = 'This should fail'
	test.send_command("p /testbin/forkbomb")
	test.look_for_and_print_result(check, 5)
	test.clean_kernel()

def main():
	path = str(sys.argv[1])
	testForkBomb(path)



if __name__ == "__main__":
	main()

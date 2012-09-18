#!/usr/bin/python

import * from core

class HelloWorld:
	def testHelloWorld(path_to_kernel):
		kernel = new TestUnit(path_to_kernel)
		kernel.basic_read_test("Hello World")
		return

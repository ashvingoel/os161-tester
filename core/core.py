#!/usr/bin/python

import pexpect
import sys

class TestUnit:
	#Implicit assumptions, sys161 is in path
	def __init__(self, path_to_kernel, message):
		global kernel
		path = 'sys161 ' + str(path_to_kernel)
		kernel = pexpect.spawn(path)
                print message
		#kernel.logfile = sys.stdout

	#We need to wait before we can actually send a command.
	def send_command(self, cmd):
		kernel.expect('for menu')
		#The fun bit is, we need to send the command character by
		#character to the simulator, otherwise we are going to have
		#a lot of fun ;-)
		cmd_char = list(cmd)
		for i in cmd_char:
			kernel.send(i)
		kernel.send('\n')
		return

	def basic_read_test(self, result):
		try:
			kernel.expect(result)
		except pexpect.TIMEOUT, e:
			return False
		return True

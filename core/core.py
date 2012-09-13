#!/usr/bin/python

import * from pexpect

class TestUnit:
	#Implicit assumptions, sys161 is in path
	def __init__(self, path_to_kernel):
		kernel = spawn('sys161 '+path_to_kernel)
		return

	#We need to wait before we can actually send a command.
	def send_command(self, cmd):
		kernel.expect('for menu')
		#The fun bit is, we need to send the command character by
		#character to the simulator, otherwise we are going to have
		#a lot of fun ;-)
		cmd_char = list(cmd)
		for i in cmd_char:
			kernel.send(cmd_char[i])
		kernel.send('\n')
		return

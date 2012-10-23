#!/usr/bin/python

#Start off by creating a default template
#Read the files to get all the information needed
#Generate an mbox of all the emails
#use bash script to send the mbox using sendmail

import sys


def generateSalutation(utorid):
	d_line = 'Dear'
	for i in utorid:
		d_line+= " " + i
	return d_line

def generateBody(grp, asst, marks):
	b_line ='Your submission for Assignment ' + str(asst) + 'has been automarked\n\n'
	total = 0
	mark = 0
	for i in marks:
		total += i['total']
		mark += i['mark']

	b_line += 'You have scored ' + str(mark) + ' out of a possible '+ str(total) + ' marks.\n\n'
	b_line += 'You have scored: \n\n'

	for i in marks:
		b_line += i['name'] + ': ' + str(i['mark']) + ' out of ' + str(i['total']) + '\n'

	return b_line

def generateBye(TA):
	l_line = 'Please contact ' + TA + ' if you have further questions regarding your marks.\n\n'
	l_line += 'Best of luck for the next assignment.\n\n'
	l_line += 'ECE 344 TAs\n'
	return l_line

def parseMarkFile(grp):
	#filename = 'os161-mark-'+ grp +'.txt'
	filename = 'os161-mark.txt'
	f = open(filename, 'r')
	mark = []
	for l in f.readlines():
		line = l.split(',')
		mark.append({'name': line[0], 'total': line[1], 'mark': line[2]})
	f.close()
	return mark

def parseEmailFile(grp):
	filename = 'emails.txt'
	f = open(filename, 'r')
	utorid = []
	email = []
	for line in f.readlines():
		if grp in line:
			l = line.split(',')
			i = 0
			for value in l:
				if i == 0:
					continue
					i += 1
				elif i % 2 == 1:
					#Must be utorid
					utorid.append(value)
				else:
					#Must be email id
					email.append(value)
				i += 1
	return (utorid, email)

def main():
	asst = str(sys.argv[1])
	(utor, em) = parseEmailFile('001')
	for i in utor:
		print i
	for i in em:
		print i

if __name__ == "__main__":
	main()

#!/usr/bin/python

import re
import argparse

def insertUser(username , password):

	# Blacklists

	if str(type(username)) != "<type 'str'>" or str(type(password)) != "<type 'str'>":
		exit(1)

	if not re.match("^[a-zA-Z0-9_]*$", username):
		exit(1)

	if not re.match("^[a-zA-Z0-9_]*$", password):
		exit(1)

	if len(username) <= 2 or len(password) <= 2:
		exit(1)

	userfile = open("user_db/14c4b06b824ec593239362517f538b29.db" , 'a')
	passwordfile = open("user_db/5f4dcc3b5aa765d61d8327deb882cf99.db" , 'a')

	userfile.write(username + "$$$$$")
	passwordfile.write(password + "$$$$$")

	userfile.close()
	passwordfile.close()

def getUser(username , password):

	# Blacklists

        if str(type(username)) != "<type 'str'>" or str(type(password)) != "<type 'str'>":
                exit(1)

        if not re.match("^[a-zA-Z0-9_]*$", username):
                exit(1)

        if not re.match("^[a-zA-Z0-9_]*$", password):
                exit(1)

        if len(username) <= 2 or len(password) <= 2:
                exit(1)

        userfile = open("user_db/14c4b06b824ec593239362517f538b29.db" , 'r')
        passwordfile = open("user_db/5f4dcc3b5aa765d61d8327deb882cf99.db" , 'r')

	# Search

	index = -404 #Not found

	userlist = userfile.read().split("$$$$$")
	userfile.close()

	userlist[0] = userlist[0][1:]

	print userlist
	for i in range(0 , len(userlist)):
		if userlist[i] == username:
			index = i
			print str(i)
			break

	if index == 404:
		return "ERRNO 101: NO_USER_FOUND"

	passlist = passwordfile.read().split("$$$$$")
	passlist[0] = passlist[0][1:]
	print passlist
	passwordfile.close()

	if passlist[index] == password:
		return str(username) + " ~|~ " + str(password) + " ~|~ " + str(index)
	else:
		return "ERRNO 102: INCORRECT_PASSWORD"

def rmUser(username , password):

        # Blacklists

        if str(type(username)) != "<type 'str'>" or str(type(password)) != "<type 'str'>":
                exit(1)

        if not re.match("^[a-zA-Z0-9_]*$", username):
                exit(1)

        if not re.match("^[a-zA-Z0-9_]*$", password):
                exit(1)

        if len(username) <= 2 or len(password) <= 2:
                exit(1)
	_EXITCODE = getUser(username , password)
	_strproc = _EXITCODE.split(" ~|~ ")

	# A valid _strproc should have 3 fields after splitting on the mystic pipe

	if len(_strproc) != 3:
		print _EXITCODE
		exit(1)

	# Open with 'w' to overwrite
	userfile = open("user_db/14c4b06b824ec593239362517f538b29.db" , 'w')
        passwordfile = open("user_db/5f4dcc3b5aa765d61d8327deb882cf99.db" , 'w')

	userlist = userfile.read().split("\n").pop(_strproc[2])
	passlist = passwordfile.read().split("\n").pop(_strproc[2])

	# Rebuild strings

	user_writeout = ""
	pass_writeout = ""
	for user in userlist:
		user_writeout += user + "\n"

	for p in pass_writeout:
		pass_writeout += p + "\n"

	userfile.write(user_writeout)
	passwordfile.write(pass_writeout)
	userfile.close()
	passwordfile.close()

def main():
	parser = argparse.ArgumentParser(description='whaTDB.py : A Python Database Handler written by Ethan Cheng')
	parser.add_argument('-a','--add', help='Add a user to database',required=False)
	parser.add_argument('-r','--remove', help='Remove a user from database',required=False)
	parser.add_argument('-s','--show', help='Show data for a user',required=False)
	parser.add_argument('-u','--username', help='Specify Username',required=True)
	parser.add_argument('-p','--password', help='Specify Password',required=False)

	args = parser.parse_args()
	if args.username:
		if args.password:
			if args.add:
				insertUser(args.username , args.password)
			elif args.remove:
				rmUser(args.username , args.password)
			elif args.show:
				print getUser(args.username , args.password)
		else:
			print '-p <password> is a required flag'
	else:
		print '-u <username> is a required flag'

if __name__ == "__main__":
	main()

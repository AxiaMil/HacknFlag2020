#!/usr/bin/python3

import random
import string
import time
from threading import Thread
import hashlib
import sys

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def check():
	time.sleep(1)
	if (user_md5 == hashlib.md5(random_string.encode('utf-8')).hexdigest()):
		print("H@5h35_r_@_5cAm_LOL_1457465344523")
	elif user_md5 == 'a':
		print("lol")
	else:
		print("Too slow")
		sys.exit


user_md5 = None
random_string = randomString(20)
Thread(target = check).start()
print("Give me the md5 of this string: " + random_string)
user_md5 = input()

#!/usr/bin/env python2
import sys

password = "fjisodfsojfdsoijfsojdiijof231c2rm@#$$@V" #unguessable 
counter = 0
guess = False

while not guess:
    i = counter % 20
    print "Enter A for flag"
    sys.stdout.flush()
    user = str(raw_input())
    if user != 'A':
        quit()
    counter += 1
    if user == password or counter >= 1000:
        print "Here's the flag: HNF{just_pur3_brut3_str3ngth!!}"
        sys.stdout.flush()
        guess = True

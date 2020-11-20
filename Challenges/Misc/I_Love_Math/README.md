# I Love Math

## Question Text

Math like ez oni, but is it though... submit the flag format with the LNC{}

*Creator - @AxiaMil*

### Hints (Optional)
1. z1 + z1 + z1 
2. teeorbfuuskatee the source code
4. the wordlength is 23 and the last 5 words is _W0rLD

## Setup Guide
1. Host the index file (static website)

## Distribution
- NA

## Solution
1. Start by deobfuscating the code
2. Since the flag must be from 0At3_LDfcsWrbuO
3. We are also presented with multiple rules and checking sequence
```
var i = e['hjF8D'][split]('`'); //Splits 3`2`4`5`0`1 into a list [3,2,4,5,0,1]
      var u = 0x0; // u = 0
      while (!![]) { // While True
          switch (i[u++]) { //Start from case 3 then 2 then 4 and end at 5 then 0 and lastly 1
              case 0: // Runs second last
                  for (var z = 0; z < l[length]; z++) {
                      q = e['67dD3'](q, l[charCodeAt](z)); // sum(q, ord(l[z]))
                      w = e['gYu12'](w, l[charCodeAt](z)); // XOR(w, ord(l[z]))
                      r = ((r << 0x5) - r) + (l[charCodeAt](z) - 48) // r = leftShift(r, 5) + ord(l[z]) - 48
                  };
                  continue;
              case 1: // Runs Last (This case checks for n so if we are able to decode this we will get n)
              		  // password = pwd && character = char && 
                  if ((!/[^0At3_LDfcsWrbuO]/ [test](n)) && // N must belong from this range of characters '0At3_LDfcsWrbuO'
                  	 (q == 0x7B0) && // Checks if q = 7B0
                  	 (w == 0x42) &&  // Check if w = 0x42
                  	 (r == 0x4635E068) && //checks if r = 0x4635E068
                  	 (n[charCodeAt](0x3) - n[charCodeAt](0x1) == 0x36) && // the 4th char of pwd minus the 2 char you will get 54
                  	 (n[charCodeAt](0x1) == n[charCodeAt](0x0)) && // the 1st char of pwd = 2nd char of pwd
                  	 (n[charCodeAt](0x6) == 0x63) && // the 7th char of pwd = c
                  	 (n[charCodeAt](0x7) == 0x41) && // the 8th char of pwd = A
                  	 (n[charCodeAt](0x8) == 0x74) && // the 9th char of pwd = t
                  	 (n[charCodeAt](0x15) == 0x4c) && // the 16th char of pwd = L
                  	 (n[charCodeAt](0x2) == 0x62) && // the 3rd char of pwd = b
                  	 (n[charCodeAt](0x9) == 0x33) && // the 10th char of pwd = 3
                  	 (n[charCodeAt](0x8) == n[charCodeAt](0xd)) && // the 9th char of pwd = 13th char of pwd
                  	 (n[charCodeAt](0x4) == n[charCodeAt](0xc)) && // the 5th char of pwd = 12th char of pwd
                  	 (n[charCodeAt](0xb) == n[charCodeAt](0xf)) && // the 11th char of pwd = 15th char of pwd
                  	 ((n[_0x20b1[7]] << 0x2) == n[charCodeAt](0x12) + 0x5) && // 
                  	 (n[charCodeAt](0x13) == n[charCodeAt](0xf))) // the 14th char of pwd = 15th char of pwd
                  {
                      alert('Good Job! The Flag is CIC{' + n + '}'); // From here you will understand that n is the flag
                      return
                  } 
                  else 
                  {
                      alert(_0x20b1[15]);
                      return
                  };
```
4. From the regex you can see that the password starts with 0 (^0)
5. Lets start by getting all the simple clues given 
6. 7th char of the password is c
8. 8th char of the password is A
9. 9th char of the password is t
10. 10th char of the password is 3
11. 9th char = 13 char hence 13th char of the password is t
12. 11th = 14th = 15th
13. 5th = 12th
14. the 4th char of pwd minus the 2 char you will get 54
15. Lets create a simple python script to find the possibilities
```
a = '0At3_LDfcsWrbuO'
a = '0At3_LDfcsWrbuO'
for i in a:
  for ii in a:
    if(ord(i)-ord(ii)==0x36):
      print(i,ii)
```
16. From this it gave me an output of ('f', '0')
17. Therefore, we know that 4th char of the password is f and the 2nd char is 0
18. Lets start creating the flag and put # if the value is still unknown
19. n = flag = 00#f##cAt3##t##l (thats the total amount that we know but we do not know the length of the flag)
20. Looking at how the website checks the code, bruteforcing is necessary as the >> shifting of bits is close to impossible to reverse when looped 
21. So lets make our own function to bruteforce the password 
22. I would be using z3 to predict the output using the given rules and bruteforcing the rest of the value by checking them to the given value of case 0
```
from z3 import *
import struct

# calculate e,f,d for a given input password
def calc(m):
    e = 0
    f = 0
    d = 0
    for i in xrange(0, len(m)):
        c = ord(m[i])
        e += c
        f ^= c
        d = (struct.unpack("i",struct.pack("I",(d << 0x5)&0xffffffff))[0] - d) + c - 48;
    return d,e,f

# try z3 for a given password length
def check(length):
    print("Try to find a valid password for length: {}".format(length))
    s =  Solver()
    
    # a character has to be one of: 0At3_LDfcsWrbuO
    def is_valid(x):
        return Or(
                (x == ord('0')),
                (x == ord('A')),
                (x == ord('t')),
                (x == ord('3')),
                (x == ord('_')),
                (x == ord('L')),
                (x == ord('D')),
                (x == ord('f')),
                (x == ord('c')),
                (x == ord('s')),
                (x == ord('W')),
                (x == ord('r')),
                (x == ord('b')),
                (x == ord('u')),
                (x == ord('O')))

    # dynamically create a Bit vector for the password length
    vec=""
    for i in xrange(0,length):
        vec += "pw[{}] ".format(i)

    m = BitVecs(vec, 8)

    # add the rules for the alphabet to each character
    for i in xrange(0, length):
        s.add(is_valid(m[i]))

    # init e and f with 0
    e=0
    f=0

    # perform the calculations that can be solved with z3
    # d not included
    for i in xrange(0, length):
        e += m[i]
        f ^= m[i]

    # The extracted rules
    s.add(e == 0x7B0)
    s.add(f == 0x42) 
    s.add(m[0xb] == m[0xf]) 
    s.add(m[0x13] == m[0xf]) 
    s.add(m[0x1] == m[0x0])
    s.add(m[0x4] == m[0xc])
    s.add(m[0x8] == m[0xd])

    # explorative part. Set certain values by hand
    s.add(m[0] == ord('0'))
    s.add(m[1] == ord('0'))
    s.add(m[2] == ord('b'))
    s.add(m[3] == ord('f'))
    #Guess 'u' based on the word produce
    s.add(m[4] == ord('u'))
    #Guess 's' based on the word produce
    s.add(m[5] == ord('s'))
    s.add(m[6] == ord('c'))
    s.add(m[7] == ord('A'))
    s.add(m[8] == ord('t'))
    s.add(m[13] == ord('t'))
    s.add(m[18] == ord('W'))
    s.add(m[21] == ord('L'))
    

    # check if there is a solution to those rules
    while s.check() == z3.sat:
        # get a model that satisfies the rules
        model = s.model()
        out = ""
        nope = []
        #print "\n#### Model ####"
        for i in m:
            if str(i):
                out += chr(model[i].as_long()&0xff)
            nope.append(i!=model[i])

        # prevent this solution to come up again
        s.add(Or(nope[:-1]))

        # check if the password satisfies d
        d,e,f = calc(out)
        print(length, out, hex(d),hex(e),hex(f), d == 1177935976)
        if d== 1177935976 or d == 0x4635E068:
            print(out)
            exit()
    print(s.check())

for x in [23,25,26]:
    check(x)
```
23. running the above code, i got the flag `00bfuscAt3_0ut_0f_W0rLD`
### Flag
`HNF{00bfuscAt3_0ut_0f_W0rLD}`

## Recommended Reads
1. Z3

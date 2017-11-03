# delete adjacent doubles from strings
'''
import sys

s = raw_input()
# print s
print 'length of s is ', len(s)
if len(s) < 2:
    print s
else:
    fi = 0
    se = 1
    while se < len(s):
        print 'fi ', fi, 'se ', se
        if s[fi] == s[se]:
            print 'found double', s[fi], s[se]
            s = s[:fi] + s[se+1:]
            
        else:
            print 'at fi = ',  fi, ' and se = ', se, 'no double'
            fi += 1 
            se += 1

            print 'new fi ', fi, 'new se ', se
if len(s) == 0:
    print 'Empty String'
else: 
    print s

'''

import sys

def super_reduced_string(s):
    # Complete this function
    if len(s) == 0:
        return 'Empty String'
    elif len(s) < 2:
        return s
    else:
        fi = 0 
        se = 1
    while se < len(s):
        if s[fi] == s[se]: # adjacent equals
            s = s[:fi] + s[se+1:]
            s = super_reduced_string(s)
        else:
            fi += 1 
            se += 1
    if len(s) == 0:
        return 'Empty String'
    else:
        # s = super_reduced_string(s)
        return s 

s = raw_input().strip()

result = super_reduced_string(s)
print(result)

# aaabccddd

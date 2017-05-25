# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 09:09:38 2016

@author: SKamble
"""

import os
import re
from One import Create_pst

class One1(object):
    number = "aaa"
    
    def give_number(self):
        One1.number = "bbb"
        print One1.number
        
        
a = One1()
a.give_number()

def obs(f):
    lines = [line.rstrip('\n') for line in open(f)]
    print lines


print '\033[1m' + 'Hello'
x = "Suraj"
print x[-3:]


output = os.popen("swmm5  WashDOT216.inp WashDOT216.rpt WashDOT216.out").readlines()
print output
print re.sub("\x08.", "", ''.join(output))
output1 = ""
for item in output:
    
    print item

#print output1

print "\""

one = Create_pst("groof09Q1.tpl")
print "begin"
one.show_result("groof09Q1.rec", "Drain Outflow", "groof09Q1.dat")
print "end"

# -*- coding: UTF-8 -*-

import os

f = open('2_file_1.txt')
s = f.read()
f.close()
fh = open('2_file_2.txt', 'a')
fh.write(s)
fh.close 
os.remove('2_file_1.txt')

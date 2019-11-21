# -*- coding: UTF-8 -*-

import re

f = open('1_file_1.txt')
context, s = f.read(), {}
f.close()
context
letters = ['и']
for i in range(len(letters)):
  s[letters[i]] = len(re.findall('{0}'.format(letters[i]), context))
  print '{0} -> {1}'.format(letters[i], s[letters[i]])


'''
'
' @author: Ale
' @function: generate C++ header automatically
' @date: 2014-10-22
'
'''
import os
import re

f1 = open('header.cpp', 'r')
hStr = f1.read()
hStr = hStr.replace('\n', '<CR>').replace('}', '<right>').replace(')', '<right>')
#print hStr

pattern = re.compile(r'map <C-a> (.+)')
f2 = open('/home/ale/.vimrc', 'r+')
#hContent = pattern.sub(r'map <C-a> ' + hStr, f2.read())
hContent = pattern.sub(r'map <C-a> i' + hStr, f2.read())
print hContent
f2.seek(0)
f2.write(hContent)

#str1 = os.popen('bash ./auto.sh').read()

f1.close()
f2.close()

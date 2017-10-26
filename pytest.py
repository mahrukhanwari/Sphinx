import shutil
import sys

print "hello, python"
print ""
print "printing content file : test"
with open("test.txt", 'r') as fin:
   print fin.read()	
print "printing content file : xflow"
with open("xflow.txt", 'r') as fin:
    print fin.read()	
print "overwriting content"
with open('test.txt', 'w+') as output, open('xflow.txt', 'r') as input:
    while True:
        data = input.read(100000)
        if data == '':  # end of file reached
            break
        output.write(data)	
print "done !"

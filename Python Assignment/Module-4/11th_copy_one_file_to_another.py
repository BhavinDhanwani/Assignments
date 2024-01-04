# Write a Python program to copy the contents of a file to another file.

f=open("python.txt","r")
c=f.readlines()
f.close()

f2=open("python2.txt","w")
for i in c:
    f2.write(i)
f2.close()
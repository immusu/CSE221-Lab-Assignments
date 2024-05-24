#!/usr/bin/env python
# coding: utf-8

# In[1]:


infile=open("C:\\Users\\User\\Downloads\\input1.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output1.txt",'w')
s=infile.readlines()
n=int(s[0])

def stepsToZero(number,step=1):
    if number>999:
        return 'Please entry number between 0 to 999'
    temp=str(number)
    digits=[]
    for i in temp:
        digits.append(int(i))
    max_digit=max(digits)
    number=number-max_digit
    if number!=0:
        return stepsToZero(number,step+1)
    return step
    
out=str(stepsToZero(n))

outfile.write(out)

infile.close()
outfile.close()


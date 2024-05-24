#!/usr/bin/env python
# coding: utf-8

# In[1]:


infile=open("C:\\Users\\User\\Downloads\\input1.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output1.txt",'w')
s=infile.readlines()
n=int(s[0])

temp=[]
for i in range(1,len(s)):
    t=s[i].split()
    t2=[]
    for j in range(len(t)):
        if j==1:
            t2.append(int(t[j]))
    for k in range(len(t)):
        if k==0:
            t2.append(int(t[k]))
    temp.append(t2)

stemp=sorted(temp)

counter=0
f=0
outarr=[]
for i in range(len(stemp)):
    if i==0:
        outarr.append(stemp[i])
        counter+=1
        f=stemp[i][0]
    else:
        if f<=stemp[i][1]:
            outarr.append(stemp[i])
            counter+=1
            f=stemp[i][0]
    
out=''
out+=str(counter)+'\n'

for i in outarr:
    out+=str(i[1])+' '
    out+=str(i[0])+'\n'

outfile.write(out)

infile.close()
outfile.close()


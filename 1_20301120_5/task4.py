#!/usr/bin/env python
# coding: utf-8

# In[4]:


infile=open("C:\\Users\\User\\Downloads\\input4.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output4.txt",'w')
s=infile.readlines()
pairs=[]

for i in s:
    t=i.split()
    t1=[]
    for i in t:
        t1.append(int(i))
    pairs.append(t1)

outlst=[]

for pair in pairs:
    if pair==[0,0]:
        break
    else:
        counter=0
        for i in range(pair[0],pair[1]+1):
            temp=i**(1/2)
            if str(int(temp))+'.0'==str(temp):
                counter+=1
        outlst.append(counter)
        
out=''

for i in range(len(outlst)):
    if i!=len(outlst)-1:
        out+=str(outlst[i])+'\n'
    else:
        out+=str(outlst[i])
        
outfile.write(out)

infile.close()
outfile.close()


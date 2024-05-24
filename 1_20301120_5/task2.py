#!/usr/bin/env python
# coding: utf-8

# In[2]:


infile=open("C:\\Users\\User\\Downloads\\input2.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output2.txt",'w')
s=infile.readlines()
r=s[0].split()
n=int(r[0])
m=int(r[1])

temp=[]
for i in range(1,len(s)):
    t=s[i].split()
    t2=[]
    for j in t:
        t2.append(int(j))
    temp.append(t2)

stemp=sorted(temp)

lst=[]
for i in range(m):
    lst.append([])

counter=0
for i in range(n):
    c=0
    for j in range(len(lst)):
        if lst[j]==[]:
            lst[j].append(stemp[c])
            c+=1
            counter+=1
        else:
            if stemp[i][0]>=lst[j][-1][-1]:
                lst[j].append(stemp[i])
                counter+=1

outfile.write(str(counter))

infile.close()
outfile.close()


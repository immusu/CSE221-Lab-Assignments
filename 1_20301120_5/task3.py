#!/usr/bin/env python
# coding: utf-8

# In[3]:


infile=open("C:\\Users\\User\\Downloads\\input3.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output3.txt",'w')
s=infile.readlines()

n=int(s[0])
tasks=[]
calls=[]
for i in s[2]:
    calls.append(i)

temp=s[1].split()
for i in temp:
    tasks.append(int(i))

jah=0
jih=0
totaltask=''
taskstack=[]

for i in calls:
    if i=='J':
        taskstack.append(min(tasks))
        jah+=min(tasks)
        totaltask+=str(min(tasks))
        tasks.remove(min(tasks))
    elif i=='j':
        p=taskstack.pop()
        jih+=p
        totaltask+=str(p)

out=''
out+=totaltask+'\n'
out+='Jack will work for '+str(jah)+' hours'+'\n'
out+='Jill will work for '+str(jih)+' hours'

outfile.write(out)

infile.close()
outfile.close()


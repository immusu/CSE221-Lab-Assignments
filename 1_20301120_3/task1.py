#!/usr/bin/env python
# coding: utf-8

# In[1]:


infile=open("C:\\Users\\User\\Downloads\\input.txt",'r')

s=infile.readlines()
n=int(s[0])

temp=[]
for i in range(1,n+1):
    t1=s[i].split()
    t2=[]
    for i in t1:
        t2.append(int(i))
    temp.append(t2)

graph={}
for i in temp:
    graph[i[0]]=i[1:]
    
print(graph)


# In[ ]:





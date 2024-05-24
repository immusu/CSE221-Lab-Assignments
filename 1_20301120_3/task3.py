#!/usr/bin/env python
# coding: utf-8

# In[3]:


infile=open("C:\\Users\\User\\Downloads\\input.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output3.txt",'w')

s=infile.readlines()
n=int(s[0])

#from task 1--------------------------
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
#-------------------------------------
    
visited=[0]*n
printed=[]

def DFS_Visit(graph,node):
    visited[node-1]=1
    printed.append(node)
    for node1 in graph[node]:
        if node1 not in visited:
            DFS_Visit(graph,node1)
            
endPoint=12

def DFS(graph,endPoint):
    for node1 in graph:
        if node1 not in visited:
            DFS_Visit(graph,node1)

DFS(graph, 12)

out='Places: '

for i in printed:
    if i!=endPoint:
        out+=str(i)+' '
    else:
        out+=str(i)
        break

outfile.write(out)

infile.close()
outfile.close()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


infile=open("C:\\Users\\User\\Downloads\\input.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output2.txt",'w')

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
queue=[]

def BFS(visited,graph,node,endPoint):
    visited[int(node)-1]=1
    queue.append(node)
    outBFS=[]
    idx=0
    while queue!=[]:
        m=queue[idx]
        outBFS.append(m)
        if m==endPoint:
            break
        for i in graph[m]:
            if visited[int(i)-1]==0:
                visited[int(i)-1]=1
                queue.append(i)
        idx+=1
    return outBFS

temp1=BFS(visited,graph,1,12)

out='Places: '

for i in range(len(temp1)):
    if i!=len(temp1)-1:
        out+=str(temp1[i])+' '
    else:
        out+=str(temp1[i])
        
outfile.write(out)

infile.close()
outfile.close()


# In[ ]:





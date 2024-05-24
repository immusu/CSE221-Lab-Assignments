#!/usr/bin/env python
# coding: utf-8

# In[4]:


infile=open("C:\\Users\\User\\Downloads\\input4.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output4.txt",'w')

s=infile.readlines()
t=int(s[0])

temp=[]
for i in range(len(s)):
    if i!=0:
        temp.append(s[i].split())

bpoint=int(temp[0][0])
temp1=temp[:bpoint]
temp2=temp[bpoint:]

def graphMaking(arr):
    graph={}
    n1=int(arr[0][0])
    m1=int(arr[0][1])

    for i in range(1,n1+1):
        graph[i]=[]
    
    for i in range(1,m1+1):
        x=arr[i]
        graph[int(x[0])].append(int(x[1]))
        graph[int(x[1])].append(int(x[0]))
    return graph

graph1=graphMaking(temp1)
graph2=graphMaking(temp2)

visited=[0]*104
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

output1=BFS(visited,graph1,1,3)
output2=BFS(visited,graph2,1,3)

out=str(len(output1)-1)+'\n'+str(len(output2)-1)

outfile.write(out)

infile.close()
outfile.close()


# In[ ]:





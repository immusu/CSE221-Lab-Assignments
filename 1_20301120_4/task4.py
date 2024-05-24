#!/usr/bin/env python
# coding: utf-8

# In[1]:


import heapq
import math

infile=open("C:\\Users\\User\\Downloads\\input4.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output4.txt",'w')
s=infile.readlines()

temp=[]
for i in s:
    temp.append(i.split())

temp1=[]
for i in temp:
    for j in range(len(i)-1):
        if i[j] not in temp1:
            temp1.append(i[j])

temp2=[]
c=1
for i in temp1:
    temp2.append([i,c])
    c+=1

s=0
d=len(temp2)
for i in temp2:
    if i[0]=='MOTIJHEEL':
        s=i[1]
graph={}
for j in temp:
    u,v,w=j
    y=0
    z=0
    for k in temp2:
        if u==k[0]:
            y=k[1]
        elif v==k[0]:
            z=k[1]
    if str(y) in graph.keys():
        value=graph.get(str(y))
        value.append((str(z),int(w)))
        graph[str(y)]=value
    else:
        graph[str(y)]=[(str(z),int(w))]

def dijkstra(graph,source,destination):
    dist=[math.inf]*(int(destination))
    dist[source-1]=0
    prev=[None]*(destination)
    visited=[False]*(destination)
    Q=[]
    graphIsEmpty=not graph
    if graphIsEmpty==True:
        return dist,prev
    else:
        for vertex in graph:
            heapq.heappush(Q, (dist[int(vertex)-1],int(vertex)))
        graphIsEmpty=not Q
        while graphIsEmpty!=True:
            u=heapq.heappop(Q)
            graphIsEmpty=not Q
            if visited[u[1]-1]:
                continue
            visited[u[1]-1]=True
            if str(u[1]) in graph.keys():
                for v in range(len(graph[str(u[1])])):
                    alt=dist[u[1]-1]+graph[str(u[1])][v][1]
                    if alt<dist[int(graph[str(u[1])][v][0])-1]:
                        dist[int(graph[str(u[1])][v][0])-1]=alt
                        prev[int(graph[str(u[1])][v][0])-1]=u[1]
                        heapq.heappush(Q, (dist[int(graph[str(u[1])][v][0])-1],int(graph[str(u[1])][v][0])))

        return dist,prev
    
result=dijkstra(graph,s,d)

out=''
dis=result[0][-1]
out+=str(dis)
#Here, we can see that in this task the weight is given and that is why we are using Dijkstra algorithm instead of BFS.

outfile.write(out)

infile.close()
outfile.close()


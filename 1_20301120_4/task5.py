#!/usr/bin/env python
# coding: utf-8

# In[3]:


import heapq
import math

infile=open("C:\\Users\\User\\Downloads\\input5.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output5.txt",'w')
s=infile.readlines()
t=int(s[0])
graphs=[]
ns=[]
ds=[]

temp=[]
for i in range(1, len(s)):
    t=s[i].split()
    t1=[]
    for i in t:
        t1.append(int(i))
    temp.append(t1)

for i in range(len(temp)):
    if len(temp[i])==1:
        ds.append(temp[i][0])
    if len(temp[i])==2:
        ns.append(temp[i][0])
        gt=[]
        for j in range(i+1,i+1+temp[i][1]):
            gt.append(temp[j])
        graphs.append(gt)

def networkDijkstra(graph,source,destination):
    dist=[-math.inf]*(destination)
    dist[source-1]=math.inf
    prev=[None]*(destination)
    Q=[]
    graphIsEmpty=not graph
    if graphIsEmpty==True:
        return dist
    else:
        for vertex in graph:
            heapq.heappush(Q, (dist[int(vertex)-1],int(vertex)))
        graphIsEmpty=not Q
        while graphIsEmpty is not True:
            heapq._heapify_max(Q)
            u=heapq.heappop(Q)
            graphIsEmpty=not Q
            if str(u[1]) in graph.keys():
                for v in range(len(graph[str(u[1])])):
                    alt=min(dist[u[1]-1],graph[str(u[1])][v][1])
                    if alt>dist[int(graph[str(u[1])][v][0])-1]:
                        dist[int(graph[str(u[1])][v][0])-1]=alt
                        prev[int(graph[str(u[1])][v][0])-1]=u[1]
                        heapq.heappush(Q, (dist[int(graph[str(u[1])][v][0])-1],int(graph[str(u[1])][v][0])))
        return dist
    
out='' 
for i in range(len(graphs)):
    graph={}
    for j in graphs[i]:
        u,v,w=j
        if str(u) in graph.keys():
            value=graph.get(str(u))
            value.append((str(v),w))
            graph[str(u)]=value
        else:
            graph[str(u)]=[(str(v),w)]
    result=networkDijkstra(graph,ds[i],ns[i])
    temp2=''
    for i in result:
        if i==math.inf:
            temp2+='0'+' '
        elif i==-math.inf:
            temp2+='-1'+' '
        else:
            temp2+=str(i)+' '
    out+=temp2+'\n'
    
outfile.write(out)

infile.close()
outfile.close()


#!/usr/bin/env python
# coding: utf-8

# In[3]:


infile=open("C:\\Users\\User\\Downloads\\input3.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output3.txt",'w')
s=infile.readlines()
x=s[0]
y=s[1]
z=s[2]

def LCS(x,y,z):
    m=len(x)
    n=len(y)
    o=len(z)
    c=[]
    for i in range(m+1):
        c.append([])
        for j in range(n+1):
            c[i].append([0]*(o+1))
    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if (i==0 or j==0 or k==0):
                    c[i][j][k]=0
                     
                elif (x[i-1]==y[j-1] and x[i-1]==z[k-1]):
                    c[i][j][k] = c[i-1][j-1][k-1] + 1
 
                else:
                    c[i][j][k] = max(max(c[i-1][j][k], c[i][j-1][k]), c[i][j][k-1])
    return c[m][n][o]

out=str(LCS(x,y,z))

outfile.write(out)

infile.close()
outfile.close()


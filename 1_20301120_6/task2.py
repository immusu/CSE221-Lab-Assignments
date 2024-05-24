#!/usr/bin/env python
# coding: utf-8

# In[2]:


infile=open("C:\\Users\\User\\Downloads\\input2.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output2.txt",'w')
s=infile.readlines()
l=int(s[0])
x=s[1]
y=s[2]

def LCS(x,y):
    m=len(x)
    n=len(y)
    c=[]
    for i in range(m+1):
        c.append([0]*(n+1))
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                c[i][j]=0
            elif x[i-1]==y[j-1]:
                c[i][j]=c[i-1][j-1]+1
            else:
                c[i][j]= max(c[i-1][j], c[i][j-1])
    idx=c[m][n]
    lcsStr=['']*(idx+1)
    lcsStr[idx]=''
    i=m
    j=n
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            lcsStr[idx-1]=x[i-1]
            i-=1
            j-=1
            idx-=1
        elif c[i-1][j]>c[i][j-1]:
            i-=1
        else:
            j-=1
    return len(lcsStr)-1, lcsStr

temp=LCS(x,y)
keys=temp[1][:-1]

out=''
for i in keys:
    if i=="Y":
        out+="Yasnaya "
    elif i=="R":
        out+="Rozhok "
    elif i=="S":
        out+="School "
    elif i=="P":
        out+="Pochinki "
    elif i=="F":
        out+="Farm "
    elif i=="M":
        out+="Mylta "
    elif i=="H":
        out+="Shelter "
    elif i=="I":
        out+="Prison "
out+='\n'+'Correctness of prediction: '+str((temp[0]*100)/l)+'%'

outfile.write(out)

infile.close()
outfile.close()


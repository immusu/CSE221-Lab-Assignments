import time

infile=open("C:\\Users\\User\\Downloads\\input5.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output5.txt",'w')

start=time.time()

s=infile.readlines()
n=int(s[0])
temp=s[1].split()
arr=[]
for i in temp:
    arr.append(int(i))

def partition(A,p,q):
    x=A[q]
    i=p-1
    for j in range(p, q):
        if A[j]<=x:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[q]=A[q],A[i+1]
    return (i+1)

def quickSort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)

quickSort(arr,0,n-1)

out=''

for i in range(n):
    if i!=n-1:
        out+=str(arr[i])+' '
    else:
        out+=str(arr[i])
        
outfile.write(out)

end=time.time()
outfile.write('\n'+str(end-start))

def findK(arr,n,k):
    return arr[k-1]

temp2=s[2].split()
k=int(temp2[-1])

kth= findK(arr, n, k)

outfile.write('\n'+str(kth))

infile.close()
outfile.close()


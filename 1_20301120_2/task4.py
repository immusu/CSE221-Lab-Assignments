infile=open("C:\\Users\\User\\Downloads\\input4.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output4.txt",'w')
s=infile.readlines()
n=int(s[0])
arr=s[1].split()

def merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*(n1)
    R=[0]*(n2)
    for i in range(n1):
        L[i]=int(A[p+i])
    for j in range(n2):
        R[j]=int(A[q+1+j])
    i=0    
    j=0    
    k=p
    while i<n1 and j<n2 :
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
        k+=1
    while i<n1:
        A[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        A[k]=R[j]
        j+=1
        k+=1

def mergeSort(A,p,r):
    if p<r: #checking for base case
        q=(p+(r-1))//2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)
        return A
        
mergeSort(arr,0,n-1)

out=''

for i in range(n):
    if i!=n-1:
        out+=str(arr[i])+' '
    else:
        out+=str(arr[i])
        
outfile.write(out)

infile.close()
outfile.close()


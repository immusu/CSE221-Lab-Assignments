infile=open("C:\\Users\\User\\Downloads\\input3.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output3.txt",'w')
s=infile.readlines()
n=int(s[0])
ID=s[1].split()
temp1=s[2].split()
mark=s[2].split()

def insertionSort(A,n):
    for i in range(n-1):
        temp=A[i+1]
        for j in range(i,-2,-1):
            if int(A[j])<int(temp):
                A[j+1]=A[j]
            else:
                break
        A[j+1]=temp
    return A

insertionSort(mark,n)

temp2=[]
out=''

for i in range(n):
    for j in range(n):
        if mark[i]==temp1[j]:
            temp2.append(j)
            
for i in range(n):
    if i!=n-1:
        out+=ID[temp2[i]]+' '
    else:
        out+=ID[temp2[i]]
    
outfile.write(out)

infile.close()
outfile.close()


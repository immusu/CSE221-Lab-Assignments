infile=open("C:\\Users\\User\\Downloads\\input4.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output4.txt",'w')

s=infile.read()
lines=s.split('\n')
n=int(lines[0])

Astr=[]
Bstr=[]

for i in range(1,len(lines)):
    if i<=n:
        Astr.append(lines[i])
    else:
        Bstr.append(lines[i])
        
A=[[0]*n for i in range(n)]
B=[[0]*n for i in range(n)]

for j in range(len(Astr)):
    temp=Astr[j].split()
    for k in range(len(Astr)):
        A[j][k]=int(temp[k])
        
for j in range(len(Bstr)):
    temp=Bstr[j].split()
    for k in range(len(Astr)):
        B[j][k]=int(temp[k])

def matrixMultiplication(A,B):
    C=[[0]*n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j]+=A[i][k]*B[k][j]

    out=''
    for i in range(n):
        for j in range(n):
            out+=str(C[i][j])+' '
        out+='\n'
    
    outfile.write(out)
        
matrixMultiplication(A,B)
infile.close()
outfile.close()


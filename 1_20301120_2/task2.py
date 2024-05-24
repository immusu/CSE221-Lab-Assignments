infile=open("C:\\Users\\User\\Downloads\\input2.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output2.txt",'w')

s=infile.readlines()
temp=s[0].split()
n=int(temp[0])
m=int(temp[1])
arr=s[1].split()

for i in range(n):
    m=i
    for j in range(i+1,n):
        if int(arr[m])>int(arr[j]):
            m=j
    arr[i],arr[m]=arr[m],arr[i]

out=''
for i in range(m):
    if i!=m-1:
        out+=arr[i]+' '
    else:
        out+=arr[i]
        
outfile.write(out)

infile.close()
outfile.close()


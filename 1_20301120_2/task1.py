infile=open("C:\\Users\\User\\Downloads\\input1.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output1.txt",'w')

s=infile.readlines()
n=int(s[0])
arr=s[1].split()

def bubbleSort(arr):
    for i in range(len(arr)-1):
        counter=0
        for j in range(len(arr)-i-1): 
            if int(arr[j])>int(arr[j+1]):
                counter+=1
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if counter==0:
            break
    return arr

#In the bubblesorting function, we took a new counter to count the swaps of the inner for loop.
#The best case scenario is the array will be sorted.
#So, there will be no need to check the if there is any swap needed.
#For this reason, the counter is working here as a loop breaker.
#So, for the best case scenario the time complexity will be = O(n*1) = O(n)

bubbleSort(arr)
out=''
for i in range(len(arr)):
    if i==len(arr)-1:
        out+=arr[i]
    else:
        out+=arr[i]+' '
    
outfile.write(out)

infile.close()
outfile.close()


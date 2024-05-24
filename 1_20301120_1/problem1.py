infile=open("C:\\Users\\User\\Downloads\\input.txt",'r')
outfile=open("C:\\Users\\User\\Downloads\\output.txt",'w')
recfile=open("C:\\Users\\User\\Downloads\\record.txt",'w')

s=infile.readlines()
numbers=[]
strings=[]
for i in s:
    temp=i.split()
    numbers.append(temp[0])
    strings.append(temp[1])

cparity=[]
oddparity=0
evenparity=0
noparity=0
cpalindrome=[]
palindrome=0
nonpalindrome=0

for j in numbers:
    if '.' not in j:
        if int(j)%2==0:
            cparity.append('has even parity')
            evenparity+=1
        else:
            cparity.append('has odd parity')
            oddparity+=1
    else:
        cparity.append('cannot have parity')
        noparity+=1
    
for k in strings:
    if k==k[::-1]:
        cpalindrome.append('is a palindrome')
        palindrome+=1
    else:
        cpalindrome.append('is not a palindrome')
        nonpalindrome+=1
        
for l in range(len(numbers)):
    out=numbers[l]+' '+cparity[l]+' and '+strings[l]+' '+cpalindrome[l]+'\n'
    outfile.write(out)
    
recfile.write('Percentage of odd parity: '+str((oddparity/len(numbers))*100)+'%\n')
recfile.write('Percentage of even parity: '+str((evenparity/len(numbers))*100)+'%\n')
recfile.write('Percentage of no parity: '+str((noparity/len(numbers))*100)+'%\n')
recfile.write('Percentage of palindrome: '+str((palindrome/len(strings))*100)+'%\n')
recfile.write('Percentage of non palindrome: '+str((nonpalindrome/len(strings))*100)+'%\n')

infile.close()
outfile.close()
recfile.close()


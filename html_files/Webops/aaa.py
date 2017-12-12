f = open('aaa.txt','r')
mystr = f.read()
mystr = mystr.replace('aaa.txt\n','')
mystr = mystr.replace('aaa.py\n','')
# mystr = mystr.replace('.jpg','')
#mystr = mystr.replace('\n',',')
mystr_2 = mystr.split('\n')
arr = []
for line in mystr_2:
	if len(line)>0:
		arr.append(line)
print(arr)
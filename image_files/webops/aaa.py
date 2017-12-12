import os
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
		temp_1=line[0:-3]
		temp_1 = temp_1+".jpg"
		print(line,temp_1)
		os.rename(line,temp_1)
		# arr.append(line)
print(arr)
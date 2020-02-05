ENGLISH_ALPHABETS={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
ENGLISH_LEXICOGRAPHY={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}
matrix={}
matrix_xy={}
#INPUTS:
plaintext=input('Enter the plaintext to be encrypted: ').upper().replace(' ','')
key=input('Enter the value of key: ').upper().replace(' ','')
#Playfair cipher
flag1=0#i in key
flag2=0#j in key
flag3=0#i and j are not in key
flag4=0#An alphabet has been duplicated, when flag3>0
if 'I' in key:
	flag1=1
	flag3+=1
if 'J' in key:
	flag2=1
	flag3+=1
if flag3==0:
	plaintext=plaintext.replace('i','j')
#creating matrix-Adding alphabets in key
r=0
c=0
for i in key:
	if i not in matrix:
		matrix.update({i:(r,c)})
		matrix_xy.update({(r,c):i})
		c+=1
		if(c==5):
			c=0
			r+=1
#creating matrix-Adding remaining alphabets
pos=-1
replace=-1
for i in range(1,27):
	if flag3==0:
		if i==10:
			continue
		elif ENGLISH_LEXICOGRAPHY[i] not in matrix:
			matrix.update({ENGLISH_LEXICOGRAPHY[i]:(r,c)})
			matrix_xy.update({(r,c):ENGLISH_LEXICOGRAPHY[i]})
			c+=1
			if(c==5):
				c=0
				r+=1
	else:
		if flag4==0:
			if ENGLISH_LEXICOGRAPHY[i] not in matrix:
				if pos==-1:
					pos=i
					continue
				else:
					replace=i
					flag4=1
					plaintext=plaintext.replace(ENGLISH_LEXICOGRAPHY[pos],ENGLISH_LEXICOGRAPHY[replace])
					matrix.update({ENGLISH_LEXICOGRAPHY[i]:(r,c)})
					matrix_xy.update({(r,c):ENGLISH_LEXICOGRAPHY[i]})
					c+=1
					if(c==5):
						c=0
						r+=1
		else:
			matrix.update({ENGLISH_LEXICOGRAPHY[i]:(r,c)})
			matrix_xy.update({(r,c):ENGLISH_LEXICOGRAPHY[i]})
			c+=1
			if(c==5):
				c=0
				r+=1
#Displaying matrix
print("\n")
count=0
for i in matrix:
	print(i,end='')
	count+=1	
	if(count==5):
		count=0
		print()
'''
print("\n")
count=0
for i in matrix:
	print(matrix[i],end='')
	count+=1	
	if(count==5):
		count=0
		print()
'''
#Completing formatting of plaintext
for i in range(len(plaintext)-1):
	if(plaintext[i]==plaintext[i+1]) and i%2==0:
		plaintext=plaintext[:i+1]+'X'+plaintext[i+1:]
if len(plaintext)%2!=0:
	plaintext+='X'	
print("\nFormatted plaintext: ",plaintext)
'''
	PLAYFAIR CIPHER
'''
ciphertext=''
for i in range(0,len(plaintext)-1,2):
	if(matrix[plaintext[i]][0]==matrix[plaintext[i+1]][0]):
		r=matrix[plaintext[i]][0]
		c=matrix[plaintext[i]][1]
		if(c==4):
			ciphertext+=matrix_xy[(r,0)]
		else:
			ciphertext+=matrix_xy[(r,c+1)]
		c=matrix[plaintext[i+1]][1]
		if(r==4):
			ciphertext+=matrix_xy[(r,0)]
		else:
			ciphertext+=matrix_xy[(r,c+1)]
	elif(matrix[plaintext[i]][1]==matrix[plaintext[i+1]][1]):
		c=matrix[plaintext[i]][1]
		r=matrix[plaintext[i]][0]
		if(r==4):
			ciphertext+=matrix_xy[(0,c)]
		else:
			ciphertext+=matrix_xy[(r+1,c)]
		r=matrix[plaintext[i+1]][0]
		if(r==4):
			ciphertext+=matrix_xy[(0,c)]
		else:
			ciphertext+=matrix_xy[(r+1,c)]
	else:
		r=matrix[plaintext[i]][0]
		c=matrix[plaintext[i+1]][1]
		ciphertext+=matrix_xy[(r,c)]
		r=matrix[plaintext[i+1]][0]
		c=matrix[plaintext[i]][1]
		ciphertext+=matrix_xy[(r,c)]
print("\n\n\t\tCiphertext: ",ciphertext)

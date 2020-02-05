plaintext=input('Enter the plaintext to be encrypted: ').upper().replace(' ','')
key=input('Enter the value of key: ').upper().replace(' ','')
ENGLISH_ALPHABETS={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
ENGLISH_LEXICOGRAPHY={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
'''
Assumptions: 
Plaintext has only 2 letters
Key is a 2x2 matrix
'''
if(len(key)!=4):
	exit()
elif(len(plaintext)!=2):
	exit()
else:
	k=[[key[0],key[1]],[key[2],key[3]]]
	p=[[plaintext[0]],[plaintext[1]]]
	for i in range(len(k)):
		for j in range(len(k[0])):
			k[i][j]=ENGLISH_ALPHABETS[k[i][j]]
	#print(k)
	for i in range(len(p)):
		for j in range(len(p[0])):
			p[i][j]=ENGLISH_ALPHABETS[p[i][j]]
	#print(p)
	c=[[0],[0]]
	for i in range(len(k)):
		for j in range(len(p[0])):
			for l in range(len(p)):
				c[i][j]+=k[i][l]*p[l][j]
			c[i][j]%=26
			c[i][j]=ENGLISH_LEXICOGRAPHY[c[i][j]]
	print("\n\n\t\tEncrypted text: "+c[0][0]+c[1][0])
	'''
		Decryption:
	'''
	#Finding determinant
	determinant=k[0][0]*k[1][1]-k[0][1]*k[1][0]
	if determinant<0:
		determinant=26+determinant
	#Finding inverse of determinant
	i=1
	flag=0
	while(flag==0):
		if((determinant*i)%26==1):
			d_inverse=i
			flag=1
		else:
			i+=1
	#Finding adjoint
	adjoint=[[k[1][1],-1*k[0][1]],[-1*k[1][0],k[0][0]]]
	for i in range(len(adjoint)):
		for j in range(len(adjoint[0])):
			if adjoint[i][j]<0:
				adjoint[i][j]=26+adjoint[i][j]
	#Finding inverse of k
	k_inverse=[[0,0],[0,0]]
	for i in range(len(k)):
		for j in range(len(k[0])):
			k_inverse[i][j]=(d_inverse*adjoint[i][j])%26
	#Finding p as p=k_inverse*c  
	for i in range(len(c)):
		for j in range(len(c[0])):
			c[i][j]=ENGLISH_ALPHABETS[c[i][j]]
	p=[[0],[0]]
	for i in range(len(k_inverse)):
		for j in range(len(c[0])):
			for l in range(len(c)):
				p[i][j]+=k_inverse[i][l]*c[l][j]
			p[i][j]%=26
			p[i][j]=ENGLISH_LEXICOGRAPHY[p[i][j]]
	print("\n\n\t\tDecrypted text: "+p[0][0]+p[1][0])		

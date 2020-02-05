SubBytes={}
SubBytes.update({'0':{'0':'63','1':'7C','2':'77','3':'7B','4':'F2','5':'6B','6':'6F','7':'C5','8':'30','9':'01','A':'67','B':'2B','C':'FE','D':'D7','E':'AB','F':'76'}})
SubBytes.update({'1':{'0':'CA','1':'82','2':'C9','3':'7D','4':'FA','5':'59','6':'47','7':'F0','8':'AD','9':'D4','A':'A2','B':'AF','C':'9C','D':'A4','E':'72','F':'C0'}})
SubBytes.update({'2':{'0':'B7','1':'FD','2':'93','3':'26','4':'36','5':'3F','6':'F7','7':'CC','8':'34','9':'A5','A':'E5','B':'F1','C':'71','D':'D8','E':'31','F':'15'}})
SubBytes.update({'3':{'0':'04','1':'C7','2':'23','3':'C3','4':'18','5':'96','6':'05','7':'9A','8':'07','9':'12','A':'80','B':'E2','C':'EB','D':'27','E':'B2','F':'75'}})
SubBytes.update({'4':{'0':'09','1':'83','2':'2C','3':'1A','4':'1B','5':'6E','6':'5A','7':'A0','8':'52','9':'3B','A':'D6','B':'B3','C':'29','D':'E3','E':'2F','F':'84'}})
SubBytes.update({'5':{'0':'53','1':'D1','2':'00','3':'ED','4':'20','5':'FC','6':'B1','7':'5B','8':'6A','9':'CB','A':'BE','B':'39','C':'4A','D':'4C','E':'58','F':'CF'}})
SubBytes.update({'6':{'0':'D0','1':'EF','2':'AA','3':'FB','4':'43','5':'4D','6':'33','7':'85','8':'45','9':'F9','A':'02','B':'7F','C':'50','D':'3C','E':'9F','F':'A8'}})
SubBytes.update({'7':{'0':'51','1':'A3','2':'40','3':'8F','4':'92','5':'9D','6':'38','7':'F5','8':'BC','9':'B6','A':'DA','B':'21','C':'10','D':'FF','E':'F3','F':'D2'}})
SubBytes.update({'8':{'0':'CD','1':'0C','2':'13','3':'EC','4':'5F','5':'97','6':'44','7':'17','8':'C4','9':'A7','A':'7E','B':'3D','C':'64','D':'5D','E':'19','F':'73'}})
SubBytes.update({'9':{'0':'60','1':'81','2':'4F','3':'DC','4':'22','5':'2A','6':'90','7':'88','8':'46','9':'EE','A':'B8','B':'14','C':'DE','D':'5E','E':'0B','F':'DB'}})
SubBytes.update({'A':{'0':'E0','1':'32','2':'3A','3':'OA','4':'49','5':'06','6':'24','7':'5C','8':'C2','9':'D3','A':'AC','B':'62','C':'91','D':'95','E':'E4','F':'79'}})
SubBytes.update({'B':{'0':'E7','1':'CB','2':'37','3':'6D','4':'8D','5':'D5','6':'4E','7':'A9','8':'6C','9':'56','A':'F4','B':'EA','C':'65','D':'7A','E':'AE','F':'08'}})
SubBytes.update({'C':{'0':'BA','1':'78','2':'25','3':'2E','4':'1C','5':'A6','6':'B4','7':'C6','8':'E8','9':'DD','A':'74','B':'1F','C':'4B','D':'BD','E':'8B','F':'8A'}})
SubBytes.update({'D':{'0':'70','1':'3E','2':'B5','3':'66','4':'48','5':'03','6':'F6','7':'0E','8':'61','9':'35','A':'57','B':'B9','C':'86','D':'C1','E':'1D','F':'9E'}})
SubBytes.update({'E':{'0':'E1','1':'F8','2':'98','3':'11','4':'69','5':'D9','6':'8E','7':'94','8':'9B','9':'1E','A':'87','B':'E9','C':'CE','D':'55','E':'28','F':'DF'}})
SubBytes.update({'F':{'0':'8C','1':'A1','2':'89','3':'0D','4':'BF','5':'E6','6':'42','7':'68','8':'41','9':'99','A':'2D','B':'0F','C':'B0','D':'54','E':'BB','F':'16'}})
Rcon={1:[0x01,00,00,00],2:[0x02,00,00,00],3:[0x04,00,00,00],4:[0x08,00,00,00],5:[0x10,00,00,00],6:[0x20,00,00,00],7:[0x40,00,00,00],8:[0x80,00,00,00],9:[0x1B,00,00,00],10:[0x36,00,00,00]}
MixColumns=[[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
#INPUTS
plaintext=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]#[[0,0,0,0]]*4 causes binding of all 4 rows
print('Enter the 16 words of plaintext: ')
for j in range(4):
	for i in range(4):
		plaintext[i][j]=str(hex(int(input(),16))).upper().replace('0X','')#hex() takes only integer arguments, and represents the decimal number in hexadecimal
print("\n\nState matrix: ",plaintext)
print('Enter the 128bit (16 words) cipher key: ')
cipherkey=[]
for i in range(16):
	cipherkey.append(str(hex(int(input(),16))).upper().replace('0X',''))
'''
	AES Encryption
'''
print(plaintext)
print("\n\nCipherkey: ",cipherkey)
#Pre-round transformation
k=0
for j in range(4):
	for i in range(4):
		plaintext[i][j]=int(plaintext[i][j],16)
		plaintext[i][j]^=int(cipherkey[k],16)
		k+=1
		plaintext[i][j]=str(hex(plaintext[i][j])).upper().replace('0X','')
print("\n\nState matrix after pre round transformation: ",plaintext)
'''
Generate round keys
'''
Round_keys=[]
Round_keys.append(cipherkey[0:4])
Round_keys.append(cipherkey[4:8])
Round_keys.append(cipherkey[8:12])
Round_keys.append(cipherkey[12:16])
#print(Round_keys)
for i in range(1,11):
	k=4*i
	temp=Round_keys[k-1].copy()#Otherwise binding will occur
	'''
		RotWord
	'''
	temp2=temp[0]
	for l in range(0,3):
		temp[l]=temp[l+1]
	temp[3]=temp2
	for l in range(4):
		if(int(temp[l],16)>=0x10):
			temp[l]=SubBytes[temp[l][0]][temp[l][1]]
		else:
			temp[l]=SubBytes['0'][temp[l][0]]
	for l in range(4):
		temp[l]=str(hex(Rcon[k/4][l]^int(temp[l],16))).upper().replace('0X','')
	for l in range(4):
		temp[l]=str(hex(int(Round_keys[k-4][l],16)^int(temp[l],16))).upper().replace('0X','')
	Round_keys.append(temp)
	Round_keys.append([0,0,0,0])
	Round_keys.append([0,0,0,0])
	Round_keys.append([0,0,0,0])
	for l in range(1,4):
		for m in range(4):
			Round_keys[k+l][m]=str(hex(int(Round_keys[k+l-1][m],16)^int(Round_keys[k+l-4][m],16))).upper().replace('0X','')
#10 rounds
for n in range(1,11):
	'''Substitution'''
	for j in range(4):
		for k in range(4):
			if(int(plaintext[k][j],16)>=0x10):
				plaintext[k][j]=SubBytes[plaintext[k][j][0]][plaintext[k][j][1]]
			else:
				plaintext[k][j]=SubBytes['0'][plaintext[k][j]]
	print('\n\nState matrix after round ',n,' Substitution: ',plaintext)
	'''ShiftRows'''
	#row 0 is not shifted (left)
	for k in range(1,4):
		temp=plaintext[k][0]
		for j in range(0,3):
			plaintext[k][j]=plaintext[k][j+1]
		plaintext[k][3]=temp
		if(k==2):
			#row 2 is shifted twice
			temp=plaintext[k][0]
			for j in range(0,3):
				plaintext[k][j]=plaintext[k][j+1]
			plaintext[k][3]=temp
		elif(k==3):
			#row 3 is shifted thrice
			temp=plaintext[k][0]
			for j in range(0,3):
				plaintext[k][j]=plaintext[k][j+1]
			plaintext[k][3]=temp
			temp=plaintext[k][0]
			for j in range(0,3):
				plaintext[k][j]=plaintext[k][j+1]
			plaintext[k][3]=temp
	print('\n\nState matrix after round ',n,' ShiftRows: ',plaintext)
	'''MixColumns''' 
	#round 10 does not have mixer
	temp=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	if n!=10:
		for i in range(4):
			for j in range(4):
				plaintext[i][j]=int(plaintext[i][j],16)
				MixColumns[i][j]=int(str(MixColumns[i][j]),16)
		for i in range(4):
			for j in range(4):
				for k in range(4):
					if k==0:
						if MixColumns[i][k]==0x2:
							temp[i][j]=(0x2*plaintext[k][j])
							if(temp[i][j]>255):
								temp[i][j]%=256
								temp[i][j]^=0b11011
						elif MixColumns[i][k]==0x3:
							temp[i][j]=(0x2*plaintext[k][j])
							if(temp[i][j]>255):
								temp[i][j]%=256
								temp[i][j]^=0b11011
							temp[i][j]^=plaintext[k][j]
						else:
							temp[i][j]=(MixColumns[i][k]*plaintext[k][j])
					else:
						if MixColumns[i][k]==0x2:
							temp[i][j]^=(0x2*plaintext[k][j])
							if(temp[i][j]>255):
								temp[i][j]%=256
								temp[i][j]^=0b11011
						elif MixColumns[i][k]==0x3:
							temp[i][j]^=(0x2*plaintext[k][j])
							if(temp[i][j]>255):
								temp[i][j]%=256
								temp[i][j]^=0b11011
							temp[i][j]^=plaintext[k][j]
						else:
							temp[i][j]^=(MixColumns[i][k]*plaintext[k][j])
		for i in range(4):
			for j in range(4):
				plaintext[i][j]=str(hex(temp[i][j])).upper().replace('0X','')
		print('\n\nState matrix after round ',n,'MixColumns: ',plaintext)
	'''Add roundkey'''
	for i in range(4):
			for j in range(4):
				plaintext[i][j]=str(hex(int(plaintext[i][j],16)^int(Round_keys[n*4+j][i],16))).upper().replace('0X','')
	print('\n\nState matrix after round ',n,'Add RoundKey: ',plaintext)

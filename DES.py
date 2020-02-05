'''
	Define S-boxes
'''
#S-box 1
Sbox1={'00':{'0000':14,'0001':4,'0010':13,'0011':1,'0100':2,'0101':15,'0110':11,'0111':8,'1000':3,'1001':10,'1010':6,'1011':12,'1100':5,'1101':9,'1110':0,'1111':7}}
Sbox1.update({'01':{'0000':0,'0001':15,'0010':7,'0011':4,'0100':14,'0101':2,'0110':13,'0111':1,'1000':10,'1001':6,'1010':12,'1011':11,'1100':9,'1101':5,'1110':3,'1111':8}})
Sbox1.update({'10':{'0000':4,'0001':1,'0010':14,'0011':8,'0100':13,'0101':6,'0110':2,'0111':11,'1000':15,'1001':12,'1010':9,'1011':7,'1100':3,'1101':10,'1110':5,'1111':0}})
Sbox1.update({'11':{'0000':15,'0001':12,'0010':8,'0011':2,'0100':4,'0101':9,'0110':1,'0111':7,'1000':5,'1001':11,'1010':3,'1011':14,'1100':10,'1101':0,'1110':6,'1111':13}})
#S-box 2
Sbox2={'00':{'0000':15,'0001':1,'0010':8,'0011':14,'0100':6,'0101':11,'0110':3,'0111':4,'1000':9,'1001':7,'1010':2,'1011':13,'1100':12,'1101':0,'1110':5,'1111':10}}
Sbox2.update({'01':{'0000':3,'0001':13,'0010':4,'0011':7,'0100':15,'0101':2,'0110':8,'0111':14,'1000':12,'1001':0,'1010':1,'1011':10,'1100':6,'1101':9,'1110':11,'1111':5}})
Sbox2.update({'10':{'0000':0,'0001':14,'0010':7,'0011':11,'0100':10,'0101':4,'0110':13,'0111':1,'1000':5,'1001':8,'1010':12,'1011':6,'1100':9,'1101':3,'1110':2,'1111':15}})
Sbox2.update({'11':{'0000':13,'0001':8,'0010':10,'0011':1,'0100':3,'0101':15,'0110':4,'0111':2,'1000':11,'1001':6,'1010':7,'1011':12,'1100':0,'1101':5,'1110':14,'1111':9}})
#S-box 3
Sbox3={'00':{'0000':10,'0001':0,'0010':9,'0011':14,'0100':6,'0101':3,'0110':15,'0111':5,'1000':1,'1001':13,'1010':12,'1011':7,'1100':11,'1101':4,'1110':2,'1111':8}}
Sbox3.update({'01':{'0000':13,'0001':7,'0010':0,'0011':9,'0100':3,'0101':4,'0110':6,'0111':10,'1000':2,'1001':8,'1010':5,'1011':14,'1100':12,'1101':11,'1110':15,'1111':1}})
Sbox3.update({'10':{'0000':13,'0001':6,'0010':4,'0011':9,'0100':8,'0101':15,'0110':3,'0111':0,'1000':11,'1001':1,'1010':2,'1011':12,'1100':5,'1101':10,'1110':14,'1111':7}})
Sbox3.update({'11':{'0000':1,'0001':10,'0010':13,'0011':0,'0100':6,'0101':9,'0110':8,'0111':7,'1000':14,'1001':15,'1010':14,'1011':3,'1100':11,'1101':5,'1110':2,'1111':12}})
#S-box 4
Sbox4={'00':{'0000':7,'0001':13,'0010':14,'0011':3,'0100':0,'0101':6,'0110':9,'0111':10,'1000':1,'1001':2,'1010':8,'1011':5,'1100':11,'1101':12,'1110':4,'1111':15}}
Sbox4.update({'01':{'0000':13,'0001':8,'0010':11,'0011':5,'0100':6,'0101':15,'0110':0,'0111':3,'1000':4,'1001':7,'1010':2,'1011':12,'1100':1,'1101':10,'1110':14,'1111':9}})
Sbox4.update({'10':{'0000':10,'0001':6,'0010':9,'0011':0,'0100':12,'0101':11,'0110':7,'0111':13,'1000':15,'1001':1,'1010':3,'1011':14,'1100':5,'1101':2,'1110':8,'1111':4}})
Sbox4.update({'11':{'0000':3,'0001':15,'0010':0,'0011':6,'0100':10,'0101':1,'0110':13,'0111':8,'1000':9,'1001':4,'1010':5,'1011':11,'1100':12,'1101':7,'1110':2,'1111':14}})
#S-box 5
Sbox5={'00':{'0000':2,'0001':12,'0010':4,'0011':1,'0100':7,'0101':10,'0110':11,'0111':6,'1000':8,'1001':5,'1010':3,'1011':15,'1100':13,'1101':0,'1110':14,'1111':9}}
Sbox5.update({'01':{'0000':14,'0001':11,'0010':2,'0011':12,'0100':4,'0101':7,'0110':13,'0111':1,'1000':5,'1001':0,'1010':15,'1011':10,'1100':3,'1101':9,'1110':8,'1111':6}})
Sbox5.update({'10':{'0000':4,'0001':2,'0010':1,'0011':11,'0100':10,'0101':13,'0110':7,'0111':8,'1000':15,'1001':9,'1010':12,'1011':5,'1100':6,'1101':3,'1110':0,'1111':14}})
Sbox5.update({'11':{'0000':11,'0001':8,'0010':12,'0011':7,'0100':1,'0101':4,'0110':2,'0111':13,'1000':6,'1001':15,'1010':0,'1011':9,'1100':10,'1101':4,'1110':5,'1111':3}})
#S-box 6
Sbox6={'00':{'0000':12,'0001':1,'0010':10,'0011':15,'0100':9,'0101':2,'0110':6,'0111':8,'1000':0,'1001':13,'1010':3,'1011':4,'1100':14,'1101':7,'1110':5,'1111':11}}
Sbox6.update({'01':{'0000':10,'0001':15,'0010':4,'0011':2,'0100':7,'0101':12,'0110':9,'0111':5,'1000':6,'1001':1,'1010':13,'1011':14,'1100':0,'1101':11,'1110':3,'1111':8}})
Sbox6.update({'10':{'0000':9,'0001':14,'0010':15,'0011':5,'0100':2,'0101':8,'0110':12,'0111':3,'1000':7,'1001':0,'1010':4,'1011':10,'1100':1,'1101':13,'1110':11,'1111':6}})
Sbox6.update({'11':{'0000':4,'0001':3,'0010':2,'0011':12,'0100':9,'0101':5,'0110':15,'0111':10,'1000':11,'1001':14,'1010':1,'1011':7,'1100':6,'1101':0,'1110':8,'1111':13}})
#S-box 7
Sbox7={'00':{'0000':4,'0001':11,'0010':2,'0011':14,'0100':15,'0101':0,'0110':8,'0111':13,'1000':3,'1001':12,'1010':9,'1011':7,'1100':5,'1101':10,'1110':6,'1111':1}}
Sbox7.update({'01':{'0000':13,'0001':0,'0010':11,'0011':7,'0100':4,'0101':9,'0110':1,'0111':10,'1000':14,'1001':3,'1010':5,'1011':12,'1100':2,'1101':15,'1110':8,'1111':6}})
Sbox7.update({'10':{'0000':1,'0001':4,'0010':11,'0011':13,'0100':12,'0101':3,'0110':7,'0111':14,'1000':10,'1001':15,'1010':6,'1011':8,'1100':0,'1101':5,'1110':9,'1111':2}})
Sbox7.update({'11':{'0000':6,'0001':11,'0010':13,'0011':8,'0100':1,'0101':4,'0110':10,'0111':7,'1000':9,'1001':5,'1010':0,'1011':15,'1100':14,'1101':2,'1110':3,'1111':12}})
#S-box 8
Sbox8={'00':{'0000':13,'0001':2,'0010':8,'0011':4,'0100':6,'0101':15,'0110':11,'0111':1,'1000':10,'1001':9,'1010':3,'1011':14,'1100':5,'1101':0,'1110':12,'1111':7}}
Sbox8.update({'01':{'0000':1,'0001':15,'0010':13,'0011':8,'0100':10,'0101':3,'0110':7,'0111':4,'1000':12,'1001':5,'1010':6,'1011':11,'1100':0,'1101':14,'1110':9,'1111':2}})
Sbox8.update({'10':{'0000':7,'0001':11,'0010':4,'0011':1,'0100':9,'0101':12,'0110':14,'0111':2,'1000':0,'1001':6,'1010':10,'1011':13,'1100':15,'1101':3,'1110':5,'1111':8}})
Sbox8.update({'11':{'0000':2,'0001':1,'0010':14,'0011':7,'0100':4,'0101':10,'0110':8,'0111':13,'1000':15,'1001':12,'1010':9,'1011':0,'1100':3,'1101':5,'1110':6,'1111':11}})
#Conversion of S-box output
binary={0:'0000',1:'0001',2:'0010',3:'0011',4:'0100',5:'0101',6:'0110',7:'0111',8:'1000',9:'1001',10:'1010',11:'1011',12:'1100',13:'1101',14:'1110',15:'1111'}
#plaintext=list(input('Enter the plaintext to be encrypted: '))
plaintext=[]
for i in range(1,33):
	plaintext.append('1')
	plaintext.append('0')
PLAINTEXT=''
for i in plaintext:
	PLAINTEXT+=i
print("\n\n\tPlain text: ",PLAINTEXT) 
#cipherkey=list(input('Enter the value of cipherkey: '))
cipherkey=[]
for i in range(1,29):
	cipherkey.append('1')
	cipherkey.append('0')
CIPHERKEY=''
for i in cipherkey:
	CIPHERKEY+=i
print("\n\n\tCipher key: ",CIPHERKEY)
flag=0
if(len(plaintext)!=64 or len(cipherkey)!=56):
	print('Plaintext must be 64 bit and cipherkey must be 56 bit long')
	flag=1
else:
	for i in plaintext:
		if i!='0' and i!='1':
			flag=1
if flag==1:
	print('Inputs are not valid')
	exit()
else:
	'''
		
		DES Encryption
	
	Initial Permutation:	
	'''
	plaintext=[-1]+plaintext
	cipherkey=[-1]+cipherkey
	list_temp=[-1]
	m=58
	for i in range(8):
		for j in range(4):
			list_temp.append(plaintext[m-8*i+2*j])
	m=57
	for i in range(8):
		for j in range(4):
			list_temp.append(plaintext[m-8*i+2*j])
	plaintext=list_temp
	'''
	Feistel Rounds:
	'''
	for i in range(1,17):
		#print("Feistel round ",i," beginning")
		MSB_plaintext=[-1]+plaintext[1:33]
		LSB_plaintext=[-1]+plaintext[33:65]
		#Round Key generation
		if i==1:
			MSB_key=cipherkey[1:29]
			LSB_key=cipherkey[29:57]
		MSB_key=[-1]+MSB_key
		LSB_key=[-1]+LSB_key
		MSB_key=MSB_key[2:29]+[0]
		LSB_key=LSB_key[2:29]+[0]
		key_48=[-1]+MSB_key+LSB_key
		if i not in (1,2,9,16): #Second round of shifting
			MSB_key=[-1]+MSB_key
			LSB_key=[-1]+LSB_key
			MSB_key=MSB_key[2:29]+[0]
			LSB_key=LSB_key[2:29]+[0]
			key_48=[-1]+MSB_key+LSB_key
		#Key-compression table
		list_temp=[-1]
		list_temp.append(key_48[14])
		list_temp.append(key_48[17])
		list_temp.append(key_48[11])
		list_temp.append(key_48[24])
		list_temp.append(key_48[1])
		list_temp.append(key_48[5])
		list_temp.append(key_48[3])
		list_temp.append(key_48[28])
		list_temp.append(key_48[15])
		list_temp.append(key_48[6])
		list_temp.append(key_48[21])
		list_temp.append(key_48[10])
		list_temp.append(key_48[23])
		list_temp.append(key_48[19])
		list_temp.append(key_48[12])
		list_temp.append(key_48[4])
		list_temp.append(key_48[26])
		list_temp.append(key_48[8])
		list_temp.append(key_48[16])
		list_temp.append(key_48[7])
		list_temp.append(key_48[27])
		list_temp.append(key_48[20])
		list_temp.append(key_48[13])
		list_temp.append(key_48[2])
		list_temp.append(key_48[41])
		list_temp.append(key_48[52])
		list_temp.append(key_48[31])
		list_temp.append(key_48[37])
		list_temp.append(key_48[47])
		list_temp.append(key_48[55])
		list_temp.append(key_48[30])
		list_temp.append(key_48[40])
		list_temp.append(key_48[51])
		list_temp.append(key_48[45])
		list_temp.append(key_48[33])
		list_temp.append(key_48[48])
		list_temp.append(key_48[44])
		list_temp.append(key_48[49])
		list_temp.append(key_48[39])
		list_temp.append(key_48[56])
		list_temp.append(key_48[34])
		list_temp.append(key_48[53])
		list_temp.append(key_48[46])
		list_temp.append(key_48[42])
		list_temp.append(key_48[50])
		list_temp.append(key_48[36])
		list_temp.append(key_48[29])
		list_temp.append(key_48[32])
		key_48=list_temp
		#Expansion P-box
		output=[-1]+[LSB_plaintext[32]]
		for i in range(1,33):
			output.append(LSB_plaintext[i])
			if(i%4==0 and i!=32):
				output.append(LSB_plaintext[i+1])
				output.append(LSB_plaintext[i])
		output.append(LSB_plaintext[1])
		#DES FUNCTION
		output_DESfunction=[-1]
		for i in range(1,49):
			if(key_48[i]==output[i]):
				output_DESfunction.append('0')
			else:
				output_DESfunction.append('1')
		#8 S-Boxes
		output_Sboxes=[-1]
		list_temp=[-1]+output_DESfunction[1:7]
		output_Sboxes+=list(binary[Sbox1[list_temp[6]+list_temp[1]][list_temp[2]+list_temp[3]+list_temp[4]+list_temp[5]]])
		list_temp=[-1]+output_DESfunction[7:13]
		output_Sboxes+=list(binary[Sbox2[list_temp[6]+list_temp[1]][list_temp[2]+list_temp[3]+list_temp[4]+list_temp[5]]])
		list_temp=[-1]+output_DESfunction[13:19]
		output_Sboxes+=list(binary[Sbox3[list_temp[6]+list_temp[1]][list_temp[2]+list_temp[3]+list_temp[4]+list_temp[5]]])
		list_temp=[-1]+output_DESfunction[19:25]
		output_Sboxes+=list(binary[Sbox4[list_temp[6]+list_temp[1]][list_temp[2]+list_temp[3]+list_temp[4]+list_temp[5]]])
		list_temp=[-1]+output_DESfunction[25:31]
		output_Sboxes+=list(binary[Sbox5[list_temp[6]+list_temp[1]][list_temp[2]+list_temp[3]+list_temp[4]+list_temp[5]]])
		list_temp=[-1]+output_DESfunction[31:37]
		output_Sboxes+=list(binary[Sbox6[list_temp[6]+list_temp[1]][list_temp[2]+list_temp[3]+list_temp[4]+list_temp[5]]])
		list_temp=[-1]+output_DESfunction[37:43]
		output_Sboxes+=list(binary[Sbox7[list_temp[6]+list_temp[1]][list_temp[2]+list_temp[3]+list_temp[4]+list_temp[5]]])
		list_temp=[-1]+output_DESfunction[43:49]
		output_Sboxes+=list(binary[Sbox8[list_temp[6]+list_temp[1]][list_temp[2]+list_temp[3]+list_temp[4]+list_temp[5]]])
		#straight P-box
		list_temp=[-1]
		list_temp.append(output_Sboxes[16])
		list_temp.append(output_Sboxes[7])
		list_temp.append(output_Sboxes[20])
		list_temp.append(output_Sboxes[21])
		list_temp.append(output_Sboxes[29])
		list_temp.append(output_Sboxes[12])
		list_temp.append(output_Sboxes[28])
		list_temp.append(output_Sboxes[17])
		list_temp.append(output_Sboxes[1])
		list_temp.append(output_Sboxes[15])
		list_temp.append(output_Sboxes[23])
		list_temp.append(output_Sboxes[26])
		list_temp.append(output_Sboxes[5])
		list_temp.append(output_Sboxes[18])
		list_temp.append(output_Sboxes[31])
		list_temp.append(output_Sboxes[10])
		list_temp.append(output_Sboxes[2])
		list_temp.append(output_Sboxes[8])
		list_temp.append(output_Sboxes[24])
		list_temp.append(output_Sboxes[14])
		list_temp.append(output_Sboxes[32])
		list_temp.append(output_Sboxes[27])
		list_temp.append(output_Sboxes[3])
		list_temp.append(output_Sboxes[9])
		list_temp.append(output_Sboxes[19])
		list_temp.append(output_Sboxes[13])
		list_temp.append(output_Sboxes[30])
		list_temp.append(output_Sboxes[6])
		list_temp.append(output_Sboxes[22])
		list_temp.append(output_Sboxes[11])
		list_temp.append(output_Sboxes[4])
		list_temp.append(output_Sboxes[25])
		output_straightPbox=list_temp
		#XOR
		new_LSB=[-1]
		for i in range(1,33):
			if MSB_plaintext[i]==output_straightPbox[1]:
				new_LSB.append('0')
			else:
				new_LSB.append('1')
		new_MSB=LSB_plaintext
		#Feistel round output:
		plaintext=[-1]+new_MSB[1:33]+new_LSB[1:33]
		#print("Feistel round ending...")
	'''
	Final Permutation:
	'''
	list_temp=[]
	list_temp.append(plaintext[40])
	list_temp.append(plaintext[8])
	list_temp.append(plaintext[48])
	list_temp.append(plaintext[16])
	list_temp.append(plaintext[56])
	list_temp.append(plaintext[24])
	list_temp.append(plaintext[64])
	list_temp.append(plaintext[32])
	list_temp.append(plaintext[39])
	list_temp.append(plaintext[7])
	list_temp.append(plaintext[47])
	list_temp.append(plaintext[15])
	list_temp.append(plaintext[55])
	list_temp.append(plaintext[23])
	list_temp.append(plaintext[63])
	list_temp.append(plaintext[31])
	list_temp.append(plaintext[38])
	list_temp.append(plaintext[6])
	list_temp.append(plaintext[46])
	list_temp.append(plaintext[14])
	list_temp.append(plaintext[54])
	list_temp.append(plaintext[22])
	list_temp.append(plaintext[62])
	list_temp.append(plaintext[30])
	list_temp.append(plaintext[37])
	list_temp.append(plaintext[5])
	list_temp.append(plaintext[45])
	list_temp.append(plaintext[13])
	list_temp.append(plaintext[53])
	list_temp.append(plaintext[21])
	list_temp.append(plaintext[61])
	list_temp.append(plaintext[29])
	list_temp.append(plaintext[36])
	list_temp.append(plaintext[4])
	list_temp.append(plaintext[44])
	list_temp.append(plaintext[12])
	list_temp.append(plaintext[52])
	list_temp.append(plaintext[20])
	list_temp.append(plaintext[60])
	list_temp.append(plaintext[28])
	list_temp.append(plaintext[35])
	list_temp.append(plaintext[3])
	list_temp.append(plaintext[43])
	list_temp.append(plaintext[11])
	list_temp.append(plaintext[51])
	list_temp.append(plaintext[19])
	list_temp.append(plaintext[59])
	list_temp.append(plaintext[27])
	list_temp.append(plaintext[34])
	list_temp.append(plaintext[2])
	list_temp.append(plaintext[42])
	list_temp.append(plaintext[10])
	list_temp.append(plaintext[50])
	list_temp.append(plaintext[18])
	list_temp.append(plaintext[58])
	list_temp.append(plaintext[26])
	list_temp.append(plaintext[33])
	list_temp.append(plaintext[1])
	list_temp.append(plaintext[41])
	list_temp.append(plaintext[9])
	list_temp.append(plaintext[49])
	list_temp.append(plaintext[17])
	list_temp.append(plaintext[57])
	list_temp.append(plaintext[25])
	ciphertext=list_temp
	CIPHERTEXT=''
	for i in ciphertext:
		CIPHERTEXT+=i
	print('\n\n\tCipher text: ',CIPHERTEXT)

MixColumns=[[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
#INPUTS
plaintext=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print('Enter the 16 words of plaintext: ')
for j in range(4):
	for i in range(4):
		plaintext[i][j]=str(hex(int(input(),16))).upper().replace('0X','')
#print("\n\nState matrix: ",plaintext)
for j in range(4):
	for i in range(4):
		print(plaintext[j][i],'\t',end='')
	print()
#Plaintext
temp=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(4):
	for j in range(4):
		plaintext[i][j]=int(plaintext[i][j],16)
		MixColumns[i][j]=int(str(MixColumns[i][j]),16)
print('\n\nApplying MixColumns transformation:\n')
for i in range(4):
	for j in range(4):
		for k in range(4):
			if k==0:
				print('(',MixColumns[i][k],'*',str(hex(plaintext[k][j])).upper().replace('0X',''),')',end='')
			else:
				print(' ^ (',MixColumns[i][k],'*',str(hex(plaintext[k][j])).upper().replace('0X',''),')',end='')
		print('\t', end='')
	print()
print('\n\nFinal result of transformation: ')#Final result in hexadecimal
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
		temp[i][j]=str(hex(temp[i][j])).upper().replace('0X','')
		print(temp[i][j],'\t',end='')
	print()
print('\n\n')
		

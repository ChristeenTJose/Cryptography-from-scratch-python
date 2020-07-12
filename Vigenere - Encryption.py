C2I=dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',range(26)))
I2C=dict(zip(range(26),'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
#INPUTS
plaintext=input('Enter the plaintext to be encrypted: ').upper()
key=input('Enter the value of key to be used: ').upper().replace(' ','')
l1=len(plaintext)
l2=len(key)
spaces=[i for i in range(l1) if plaintext[i]==' ']
plaintext2=plaintext.replace(' ','')
l1=len(plaintext2)
if l2>l1:
	key=key[:l1]
else:
	for i in range(l2,l1):#Does not get executed when l1 == l2
		key+=key[i%l2]
#Vigenere Cipher
ciphertext=[I2C[(C2I[plaintext2[i]] + C2I[key[i]])%26] for i in range(l1)]
for i in spaces:
	ciphertext.insert(i,' ')
ciphertext=''.join(ciphertext)
#OUTPUTS
print('\n\n\t\tPlaintext:  ',plaintext)
print('\n\n\t\tCiphertext: ',ciphertext)
		
		
	

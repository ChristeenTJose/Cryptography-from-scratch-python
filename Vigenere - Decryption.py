C2I=dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',range(26)))
I2C=dict(zip(range(26),'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
#INPUTS
ciphertext=input('Enter the ciphertext: ').upper()
key=input('Enter the value of key to be used: ').upper().replace(' ','')
l1=len(ciphertext)
l2=len(key)
spaces=[i for i in range(l1) if ciphertext[i]==' ']
ciphertext2=ciphertext.replace(' ','')
l1=len(ciphertext2)
if l2>l1:
	key=key[:l1]
else:
	for i in range(l2,l1):#Does not get executed when l1 == l2
		key+=key[i%l2]
#Vigenere Cipher
plaintext=[I2C[(C2I[ciphertext2[i]] - C2I[key[i]])%26] for i in range(l1)]
for i in spaces:
	plaintext.insert(i,' ')
plaintext=''.join(plaintext)
#OUTPUTS
print('\n\n\t\tCiphertext: ',ciphertext)
print('\n\n\t\tPlaintext:  ',plaintext)


C2I=dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',range(26)))
I2C=dict(zip(range(26),'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
#INPUTS
plaintext=input('Enter the plaintext to be encrypted: ').upper()
key=int(input('\nEnter the value of key to be used: '))
#CEASAR CIPHER
ciphertext=[]
for word in plaintext.split(' '):
	ciphertext.append(''.join([I2C[(C2I[i]+key)%26] for i in word]))
ciphertext=' '.join(ciphertext)
#OUTPUTS
print('\n\n\t\tPlaintext:  ',plaintext)
print('\n\n\t\tCiphertext: ',ciphertext)

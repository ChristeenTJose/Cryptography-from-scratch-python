C2I=dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',range(26)))
I2C=dict(zip(range(26),'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
#INPUTS
ciphertext=input('Enter the ciphertext: ').upper()
key=int(input('\nEnter the value of key to be used: '))
#CEASAR CIPHER
plaintext=[]
for word in ciphertext.split(' '):
	plaintext.append(''.join([I2C[(C2I[i]-key)%26] for i in word]))
plaintext=' '.join(plaintext)
#OUTPUTS
print('\n\n\t\tCiphertext: ',ciphertext)
print('\n\n\t\tPlaintext:  ',plaintext)

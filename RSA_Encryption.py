plain=int(input('Enter the plaintext value to be encrypted: '))
n=int(input('Enter the public key component n of receiver: '))
e=int(input('Enter the pubic key component e of receiver: '))
cipher=(plain**e)%n
print('\n\n\t\tEncrypted Ciphertext is: ',cipher)

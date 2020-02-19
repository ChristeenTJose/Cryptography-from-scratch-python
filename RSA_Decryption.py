cipher=int(input('Enter the ciphertext value to be decrypted: '))
n=int(input('Enter your public key component n: '))
d=int(input('Enter your private key d: '))
plain=(cipher**d)%n
print('\n\n\t\tDecrypted Plaintext is: ',plain)


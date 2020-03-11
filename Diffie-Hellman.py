print('Diffie-Hellman Key Exchange Protocol\n')
p=int(input('Enter the value of large prime number p: '))
g=int(input('Enter the value of g (primitive root of p): '))
print('\nFor User A')
x=int(input('Choose a large random number x such that 0<=x<=(p-1): '))
print('\nFor User B')
R1=(g**x)%p
y=int(input('Choose a large random number y such that 0<=y<=(p-1): '))
R2=(g**y)%p
#A sends R1 to B
#B sends R2 to A
print('\nFor User A')
KA=(R2**x)%p
print('Symmetric key: ',KA)
print('\nFor User B')
KB=(R1**y)%p
print('Symmetric key: ',KB)

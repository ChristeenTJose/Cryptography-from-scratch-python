print('Man in the middle attack during Diffie-Hellman Key Exchange Protocol\n')
p=int(input('Enter the value of large prime number p: '))
g=int(input('Enter the value of g (primitive root of p): '))
print('\nFor User A')
x=int(input('Choose a large random number x such that 0<=x<=(p-1): '))
R1=(g**x)%p
print('\nFor User B')
y=int(input('Choose a large random number y such that 0<=y<=(p-1): '))
R2=(g**y)%p
print('\nFor User C (ATTACKER)')
z=int(input('Choose a large random number z such that 0<=z<=(p-1): '))
R3=(g**z)%p
#A sends R1 to B
#C Intercepts and Retransmitts to B
#B sends R2 to A
#C Intercepts and Retransmitts to A
print('\nFor User A')
KA=(R3**x)%p
print('Symmetric key: ',KA)
print('\nFor User B')
KB=(R3**y)%p
print('Symmetric key: ',KB)
print('\nFor Attacker C')
KCA=(R1**z)%p
print('Symmetric key (with A): ',KCA)
KCB=(R2**z)%p
print('Symmetric key (with B): ',KCB)

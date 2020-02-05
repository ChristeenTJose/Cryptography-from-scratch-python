Key_index={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
Plain_text={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
English_lexicography={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
Vigenere_Square={}
for i in range(26):
	for j in range(26):
		Vigenere_Square.update({i*26+j:English_lexicography[(j+i)%26]})
		#print(Vigenere_Square[i*26+j],end='')
	#print()
#INPUTS:
plaintext=input('Enter the plaintext to be encrypted: ').upper().replace(' ','')
key=input('Enter the value of key: ').lower()
#VIGENERE CIPHER
temp=key
for i in range(len(key),len(plaintext)):
	temp+=key[i%len(key)]
key=temp
print('\n\t\tEncrypted message: ',end='')
ciphertext=''
for i in range(len(key)):
		ciphertext+=Vigenere_Square[Key_index[key[i]]*26+Plain_text[plaintext[i]]]
print(ciphertext)
print('\n\t\tDecrypted message: ',end='')
text=''
for i in range(len(key2)):
		text+=English_lexicography[(Plain_text[ciphertext[i]]-Key_index[key2[i]])%26]
print(text)

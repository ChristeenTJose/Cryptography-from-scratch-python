p=int(input('Enter the first prime number (p): '))
q=int(input('Enter the second prime number (q): '))
n=p*q
PHI_of_n=(p-1)*(q-1)
print('Select Public key component e such that 1<e<',PHI_of_n,' and gcd(e,',PHI_of_n,') is 1 : ')
e=int(input())
if(e>=PHI_of_n):
	print('Selected value of public component is not less than',PHI_of_n);
	exit(1);
else:
	flag=0
	for i in range(2,e+1):
		if PHI_of_n%i==0:
			flag==1
	if(flag==1):
		print('GCD of ',e,' and ',PHI_of_n,' is not 1');
		exit(2)
	else:
		flag=0
		for i in range(PHI_of_n):
			if((e*i)%PHI_of_n==1):
				d=i
				flag=1
				break;
		if(flag==1):
			print('\n\n\t\tYour Private Key is: ',d)
			print('\n\n\t\tYour Public key component e is: ',e)
			print('\n\t\tYour Public key component n is: ',n)


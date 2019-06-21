##p=11;
##q=19;

p=input('Enter the first prime number ');
q=input('Enter the second prime number ');

m =int(p) * int(q) ;

seedg=input('The seed for the random number ');

N=input('The number of random numbers needed ');
rn=[N];
for k in range (1,int(N)):
    rn.append((int(seedg)**2) % m)
    seedg=rn[k]


print (rn)

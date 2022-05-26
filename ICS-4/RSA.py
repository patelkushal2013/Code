a=int(input("Enter A :"))
b=int(input("Enter B :"))
P=int(input("Enter Plaintext:"))

n=a*b
phi=(a-1)*(b-1)

e=0

def gcd(n1,n2):
    if n1==0:
        return n2
    elif n2==0:
        return n1
    elif n1<n2:
        return gcd(n1,n2-n1)
    elif n1>n2:
        return gcd(n1-n2,n2)
    else:
        return n1

for i in range (3,phi):
    if gcd(i,phi)==1:
        e=i
        break

d=0

for i in range(1,10):
    x=(i*phi+1)/e
    if int(x)==x:
        d=int(x)
        break
    
C=P**e % n
P1=C**d % n

print("CipherText= ",C)
print("Plaintext= ",P1)
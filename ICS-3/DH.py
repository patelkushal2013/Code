import random

def isprime(num):
    for i in range(2,int(num/2)+1):
        if num%i==0:
            return 0
    return 1
    
def getRand():
    while True:
        n=random.getrandbits(20)
        if isprime(n):
            return n
 
p=getRand()
q=getRand()

a=random.getrandbits(10)
b=random.getrandbits(10)

R=q**a % p

S=q**b % p

R_key=S ** a % p
S_key=R ** b % p

print("p = ",p)
print("q = ",q)
print("a = ",a)
print("b = ",b)
print("R = ",R)
print("S = ",S)
print("R_key = ",R_key)
print("S_key = ",S_key)
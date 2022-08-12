a=int(input('Enter 1st num: '))
b=int(input('Enter 2nd num: '))
primes = []
for i in range(a, b):
    flag = 0
    if i == 1: continue
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0: primes.append(i)
print(f"prime numbers between [{a} and {b}] are {primes}")
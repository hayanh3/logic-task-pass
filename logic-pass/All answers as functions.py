from collections import Counter

def remove_given_character(string,char):
    return string.replace(char,'') if char in string else f"{char} is not in the String"
#print(remove_given_character(input('Enter your string: '),input('Enter character to replace: ')))

def prime(a,b):
    primes=[]
    for i in range(a,b):
        flag = 0
        if i==1: continue
        for j in range(2,i):
            if i % j==0 :
                flag=1
                break
        if flag==0: primes.append(i)
    return f"prime numbers between [{a} and {b}] are {primes}"
#print(prime(int(input('Enter 1st num: ')),int(input('Enter 2nd num: '))))

def repeated_char(string,char):
    return f"{char} is repeated {Counter(string)[char]} times" if char in string else f'{char} is not in String'
print(repeated_char('haya','k'))
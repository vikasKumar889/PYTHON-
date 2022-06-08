def check_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return "not prime"
    else:
        return "prime"

#print(check_prime(10))
#print(check_prime(11))
#print(check_prime(5))
for i in range(2,100):
    out = check_prime(i)
    print(i,out)

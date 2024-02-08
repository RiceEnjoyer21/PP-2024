def filter_prime(x):
    primes = []
    for num in x:
        if num > 1:
            check = True
            for i in range(2, int(num/2) + 1):
                if num % i == 0:
                    check = False
                    break
            if check:
                primes.append(num)
    return primes

                    
x = list(map(int, input().split()))

print(filter_prime(x))




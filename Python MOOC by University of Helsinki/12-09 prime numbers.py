'''
Please write a generator function prime_numbers() which 
creates a new generator. The generator should return new
prime numbers, one by one in sequence, from 2 onwards. 
This generator never terminates. It will generate numbers 
for as long as they are needed.
'''

# Write your solution here
def prime_numbers():
    def isPrime(num, plist):
        if num < 2:
            return False
        limit = int(num ** 0.5) + 1
        for p in plist:
            if p >= limit:
                break
            if not num % p:
                return False

        return True

    curr, primes = 2, []
    while True:
        if isPrime(curr, primes):
            primes.append(curr)
            yield curr
        curr += 1

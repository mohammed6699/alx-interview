#!/usr/bin/python3
def isWinner(x, nums):
    if not nums or x < 1:
        return None
    
    def Sieve(max_n):
        primes = [True] * (max_n + 1)
        primes[0] = primes[1] = False
        for i in range (2, int(max_n**0.5) + 1):
            if primes[i]:
                for j in range (i * i, max_n + 1, i):
                    primes[j] = False
        return primes
    
    max_n = max(nums)
    primes = Sieve(max_n)
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    maria_Wins = 0
    ben_Wens = 0
    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben_Wens += 1 
        else:
            maria_Wins += 1
    
    if maria_Wins > ben_Wens:
        return "Maria"
    elif ben_Wens > maria_Wins:
        return "Ben"
    else:
        return None
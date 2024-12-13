#!/usr/bin/python3
"""
    Create a helper function to precompute the prime numbers up to the maximum value of n
    or each value of n, simulate the game to determine the winner by tracking turns and removing primes and their multiples
    Tally the wins for Maria and Ben across all rounds.
    Compare the win counts and return the name of the player with the most wins, or None if they have equal wins.
"""
def isWinner(x, nums):
    """
        x: a number 
        nums: arrays of n
        if nums or x is valiable retrun num
        else return false
    """
    if not nums or x < 1:
        return None
    
    def Sieve(max_n):
        """
            precompute prime numbers up to the maximum n
            max_n: max number of sieve
           return name of the winner
        """
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
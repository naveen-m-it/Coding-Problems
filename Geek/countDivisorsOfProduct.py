from collections import defaultdict
class Solution:
    def SieveOfEratosthenes(self,largest, prime):
 
    # Create a boolean array "isPrime[0..n]" and initialize
    # all entries it as true. A value in isPrime[i] will
        # finally be false if i is Not a isPrime, else true.
        isPrime = [True] * (largest + 1)
     
        p = 2
        while p * p <= largest:
     
            # If isPrime[p] is not changed, then it is a isPrime
            if (isPrime[p] == True):
     
                # Update all multiples of p
                for i in range(p * 2, largest + 1, p):
                    isPrime[i] = False
            p += 1
     
        # Print all isPrime numbers
        for p in range(2, largest + 1):
            if (isPrime[p]):
                prime.append(p)
     
    # Returns number of divisors in array
    # multiplication
    def countDivisorsMult(self,arr, n):
     
        # Find all prime numbers smaller than
        # the largest element.
        largest = max(arr)
        prime = []
        self.SieveOfEratosthenes(largest, prime)
     
        # Find counts of occurrences of each prime
        # factor
        mp = defaultdict(int)
        for i in range(n):
            for j in range(len(prime)):
                while(arr[i] > 1 and arr[i] % prime[j] == 0):
                    arr[i] //= prime[j]
                    mp[prime[j]] += 1
            if (arr[i] != 1):
                mp[arr[i]] += 1
     
        # Compute count of all divisors using counts
        # prime factors.
        res = 1
        for it in mp.values():
            res *= (it + 1)
        return res
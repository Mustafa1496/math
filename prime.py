class Prime:
    def __init__(self) :
        pass

    def check_prime(self,num):
        if num < 2: 
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def find_primes(self, start, end):
        primes = []
        for num in range(start, end + 1):
            if self.check_prime(num):
                primes.append(num)
        return primes
        
    def legendre_symbol(self, a, p):
            if not self.check_prime(p) or p == 2:
                raise ValueError("p must be an odd prime")
            ls = pow(a, (p-1)//2, p)
            return -1 if ls == p-1 else ls
    
num = Prime()
print(num.check_prime(19)) 
print(num.find_primes(10,50))
print(num.legendre_symbol(2,23))

    

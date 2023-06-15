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
        
num = Prime()
print(num.check_prime(19)) 

    

class Prime:
    def __init__(self) :
        pass

    def check_prime(self,num):
        self.num = num
        for i in range(2,int(num**0.5)):
            if num%i == 0:
                return i
        else:
            return num
        
num = Prime()
print(num.check_prime(19))

    

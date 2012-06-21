
n = 50

print "the first 50 primes:"


primeNum_count = 0


primeNum = 2


while primeNum_count < n:


    divisor_count = 0


    for i in range(1,primeNum+1):

       
        if primeNum % i == 0:
            
            divisor_count += 1


    if divisor_count == 2:
        
        print primeNum,

       
        primeNum_count += 1

   
        if primeNum_count % 10 == 0:
            
            print

   
    primeNum += 1


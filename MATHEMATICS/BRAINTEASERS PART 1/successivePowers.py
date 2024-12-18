from sympy import isprime
powers = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
basis = [x for x in range(100,1000) if isprime(x)]
for p in basis:
    for x in range(1,p):
        for i,power in enumerate(powers):
            if i==len(powers)-1:
                print('crypto{',p,',',x,'}',sep='')
            elif not (x*power)%p==powers[i+1]: break

# This script identifies a prime  p  and a value  x that satisfy a sequence of modular arithmetic conditions involving successive powers. By iterating through potential primes and candidate values, it checks whether the sequence of modular equations holds, revealing a hidden pattern or solution. The challenge focuses on modular arithmetic, iterative computations, and exploring patterns in prime-based sequences. 
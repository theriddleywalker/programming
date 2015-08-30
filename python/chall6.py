#!/usr/bin/python

#Securityoverride.org Progarmming Challenge #6

import sys
tmp = sys.argv[1]
final = []
def genprimes(num):
    x=2                         #begin all counters at 2, since 2 is first prime - skip 0,1
    isprime=1                   #assume all numbers are prime
    primes=[]                   #initialize primes list as empty list
    while x <= num:             #run through all numbers starting at 2 (the first prime) until the last number from command line arg
        y=2
        while y < x:            #run through all numbers starting at 2(the first prime) until the number just before the current number from the previous loop 
                                #(because a prime is always divisible by itself, so theirs no need to check that number) checking for primes
            if x%y==0:          #if x is divisible by number other than 1 and itself 
                isprime=0       #number is NOT prime
                break           #break from current while loop and move to next number
            isprime=1           #otherwise keep isprime variable/flag as 1/true
            y+=1
        if isprime == 1:        #check isprime flag value
            primes.append(x)    #if prime number found add to list of primes (primes list)
        x+=1
    return primes

def primefactorization(num,answer):
    for prime in genprimes(int(tmp)):
        if prime == num:
            answer.append(prime)
            print sum(answer)
            return 0
        if num%prime == 0:
            answer.append(prime)
            primefactorization(num/prime,answer)
            return 0

primefactorization(int(tmp),final)

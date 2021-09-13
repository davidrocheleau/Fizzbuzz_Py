#!/usr/bin/env python
# This program is a fizzbuzz generator for numbers divisible by 3 and/or 5
__author__ = "David Rocheleau"

__email__ = "drochele@asu.edu"

def fizzbuzz(start, stop, step):
    stop+=step
    for i in range(start,stop,step):
        ret_str = ''
        if(i%3==0):
            ret_str+='fizz'
        if(i%5==0):
            ret_str+='buzz'
        if not ret_str:
            ret_str = i
        print(ret_str)
    
def main():
    start = input('Enter start position of fizzbuzz: ')
    stop = input('Enter stop position of fizzbuzz: ')
    step = input('Enter step size for fizzbuzz: ')
    
    fizzbuzz(int(start), int(stop), int(step))
    
    print('Program has ended. Have a nice day!')
    
    
main()

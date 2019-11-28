"""
    prime.py
    Created by: Edxio Kraudy Mora
    Date: November 28, 2019
"""

#Ask user for input integer and assign the value to num
num = int (input ("Enter an integer to determine whether it is a prime number: "))

c = 0

for divisor in range (2, num + 1):

    #If the number is not prime
    if num % divisor == 0 and divisor != num:
        print("%d is not a prime number." %num)
        c += 1
        break

#If the number is prime
if c == 0:
    print("%d is a prime number." %num)

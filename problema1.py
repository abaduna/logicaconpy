

# If we list all the natural numbers below 10 that are multiples
#  of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


suma =  0
 
for i  in range(1000):
    if (i %3 ==0 or i %5 ==0 ):
        suma += i

# print(str(suma))
# Each new term in the Fibonacci sequence is generated
#  by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose
#  values do not exceed four million, find the
#   sum of the even-valued terms. 
sumaria = 0
num1 = 1
num2 = 1
while(num2 < 4000000):
    temp = num1
    num1 = num2
    num2 = num2 + temp
    sumaria = num1  
    if (num1 % 2 == 0):
        sumaria += num1
    print()
#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 

primeFactor = 1
i = 2

while i <= number:
    if number % i == 0:
        primeFactor = i
        number = number / i
    else:
        i = i + 1


print(primeFactor)



# https://projecteuler.net/problem=4#:~:text=palindromic%20number%20reads,3%2Ddigit%20numbers.



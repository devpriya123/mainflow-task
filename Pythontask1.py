#1) The sum of Two Numbers:

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
result = n1+n2
print("The sum of two number is:", result)

#2)Odd or Even:

n = int(input("Enter a number: "))
if (n % 2) == 0:
   print("n is Even")
else:
   print("n is Odd")

#3) Factorial Calculation:

import math
num = 7
factorial = 1

if num < 0:
   print("factorial does not exist")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of number is:",factorial)

# 4) Fibonacci Sequence

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

nterms = 10


if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fibo(i))


# 5)Reverse a String

s1 = "PYTHON"
s2= s1[::-1]
print(s2)


# 6) Palindrome Check

def is_palindrome(s):
  return s == s[::-1]
str = input("Enter a string: ")
if is_palindrome(str):
  print("str is a palindrome.")
else:
  print("str is not a palindrome.")


# 7)Leap Year Check

year =int(input("Enter year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print(" is a leap year")
elif (year % 4 ==0) and (year % 100 != 0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")

# 8)Armstrong Number

a = int(input("Enter a number: "))
sum = 0
temp = a
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if a == sum:
   print(a,"is an Armstrong number")
else:
   print(a,"is not an Armstrong number")

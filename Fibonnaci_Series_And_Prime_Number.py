"""
  Fibonacci Series 

  What is Fibonacci Series.
    - Each number in the sequence is the sum of the two numbers 
      that precede it. So, the sequence goes: 
      0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.

  In below program i have implemented the logic of Recursion
  to create fibonacci series. Please run the program for better
  understanding.
"""

print(30*'-','\n')
#Fibonacci series Program
print('Fibonnaci Series:\n')
def fibonacci(n):
  if n==1:
    return 1
  elif n==2:
    return 1
  elif n>2:
    return fibonacci(n-1)+fibonacci(n-2)


for i in range(1,11):
  print(i,' : ',fibonacci(i))


print(30*'-','\n')

"""
  Prime Number

  What is prime number
  - The number which is devisible by its own and 1 is know as prime 
    number.

  Note: 1 is not a prime number.
  
  e.g:
      2,3,5,7,11,13... so on.

  while creating prime number program i have notice some weird things
  so i made 3 different logics to show some which is really amazing.

"""

#Prime Number

"""
  First Logic
  
  In below function i used the same logic of Prime number which is generally 
  used in coding.

  But when i check the time difference with large number of sequence that was
  really weird. 

  To test this program is working just change the range to small value which 
  will give you clear vision of progarm.

  e.g:
    - for j in range(1,21):
  
  This will display True corresponding to the number.
"""
import time

def prime_check_v1(m):
  if m==1:
    return False
  
  for d in range(2,m):
    if m%d == 0:
      return False
  return True

t0 = time.time()
for j in range(1,10001):
  prime_check_v1(j)
  #print(j,':',prime_check(j))

t1=time.time()
print('Time Required By 1st Method:', t1-t0)



"""
  Second Logic
  
  In below function i made some changes which is very usefull to deal with large
  set of numbers.

  Modified Logic:
    - Reduce numbers of divisors.
    - To do that just find the max number of divisors using 'math library'.
    - In below logic i just find the square root of number to reduce the number
      of divisors and follow the same rule of prime number.
    - Using 'math.floor(x)' -> we will round up the x value and it will give 
      max number of divisor.

  To test this program is working just change the range to small value which will
  give you clear vision of progarm.

  e.g:
    - for j in range(1,21):
  
  This will display True corresponding to the number.

  Note:
    This is better then above but still we have to find best solution.

"""

print(30*'-','\n')

import math

def prime_check_v2(m):
  if m==1:return False

  sqrt_val = math.floor(math.sqrt(m))

  for i in range(2,sqrt_val+1):
    if m%i==0:
      return False
  return True

t0 = time.time()
for j in range(1,10001):
  #print(j,':',prime_check_v2(j))
  prime_check_v2(j)

t1=time.time()
print('Time Required By 2nd Method:', t1-t0)


"""
  Third Logic
  
  In below function i made some changes which is very usefull to deal with large 
  set of number in mean time.

  Modified Logic:
    - Just remove all even number for the number of sets, because we all
      know even are divisible by 2.
    - In below logic we have started checking number from 3.
    - As you will notice this time we have made a small change in our Loop
      i.e for k in range(3,sqrt_val+1,2):

      Changes:
        - we have started with 3.
        - As you can see we have updated our range with 2,which will always update
          your next value with additon of 2.
  
  - 2 is prime number and if number is greater than 2 check if it is divisible by 2,
    if so then it is not a prime number.
  - Thats why we started the range value with 3.

  To test this program is working just change the range to small value which will
  give you clear vision of progarm.

  e.g:
    - for k in range(1,21):
  
  This will display True corresponding to the number.

  Note:
    Till now this is the best solution for me. 
    if you know best solution then please feel free to share you Code.

  Please test all three logic and check out the time difference and you will
  get to know why i said this the best solution till now.

"""

print(30*'-','\n')

def prime_check_v3(m):
  if m==1:return False
  if m==2:return True
  if m>2 and m%2==0:return False

  sqrt_val = math.floor(math.sqrt(m))

  for k in range(3,sqrt_val+1,2):
    if m%k==0:
      return False
  
  return True

t0 = time.time()
for h in range(1,10001):
  prime_check_v3(h)
  #print(h,':',prime_check_v3(h))

t1=time.time()
print('Time Required By 3rd Method:', t1-t0)
print(30*"-")



t0 = time.time()
def prime_check_v4(l):
  for a in range(2,l):
    if(a%2==0):
      a+=1
    else:
      y=int(round(math.sqrt(a)))

      for x in range(3,y,2):
        if a%x==0:
          return False
        else:
          return True


t0 = time.time()
for h in range(1,10001):
  prime_check_v4(h)
  #print(h,':',prime_check_v3(h))

t1=time.time()
print('Time Required By 4th Method:', t1-t0)
print(30*"-")


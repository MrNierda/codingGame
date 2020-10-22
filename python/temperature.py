import sys
import math

n = int(input())  # the number of temperatures to analyse
temps = list(map(int, input().split())) # the temperatures to analyse

if(n == 0):
   print(0)
elif (n == 1):
   print(temps[0])
else:
   res = min(temps, key = lambda t: abs(t-0))
   if (abs(res) in temps):
      res = abs(res)

   print(res)

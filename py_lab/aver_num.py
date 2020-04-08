#!/usr/bin/python

N = int(input("Enter the number of numbers: "))

i = 0
_sum = 0

while i < N:
  n = int(input())
  _sum += n
  i = i + 1
  
average = _sum / N

print("Average is %f" %average)

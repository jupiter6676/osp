#!/usr/bin/python

n = int(input("Fibonacci number: "))

F0 = 0
F1 = 1
Fn = 0  # output

for i int range(1, n):
  Fn = F0 + F1
  F0 = F1
  F1 = Fn
  
  print("%d" %Fn, end=' ')  # , 이건 어떻게 하지
  
 print()
 print("F%d = %d" %(n, Fn))

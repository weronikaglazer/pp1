def sum(N):
   if N <= 1:
       return N
   else:
       return N + sum(N-1)

print(sum(10))


n = int(input()) 
if n%2 == 0:
  print("Plz Enter odd number...")
else:
  pass

for i in range(n):
    print(("H"*i).rjust(n-1)+"H"+("H"*i).ljust(n-1))


for i in range(n+1):
    print(("H"*n).center(n*2)+("H"*n).center(n*6))


for i in range((n+1)//2):
    print(("H"*n*5).center(n*6))    

for i in range(n+1):
    print(("H"*n).center(n*2)+("H"*n).center(n*6))    

for i in range(n):
    print((("H"*(n-i-1)).rjust(n)+"H"+("H"*(n-i-1)).ljust(n)).rjust(n*6))

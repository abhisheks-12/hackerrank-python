n = 5

for i in range(n):
    print(("H"*i).rjust(n-1)+"H"+("H"*i).ljust(n-1))

for i in range(n+1):
  print("H"*n + " "*n + "H"*n)

for i in range(n-2):
  print("H"*(n*3))

for i in range(n+1):
  print("H"*n + " "*n + "H"*n)


for i in range(n):
       print((("H"*(n-i)).rjust(n)+("H")+("H"*(n-i-1)).ljust(n)).rjust(n*4))





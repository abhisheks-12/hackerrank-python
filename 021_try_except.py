n = int(input())
for i in range(n):
    try:
        x,y = map(int,(input("Enter").split())
        z = x // y
        print(z)
    except ZeroDivisionError as e:
        print("bgh!")
     except  ValueError as e:
        print("value error!")

    
for test in range(int(input())):
    try:
        a,b = map(int,input().split()) 
        division_result = a // b
        print(division_result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)


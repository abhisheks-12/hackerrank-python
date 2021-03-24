# n = int(input("Enter the number:"))

# if n % 2 == 0 and n > 20 or n in range(2,5):
#     print("Not weird")

#     # if n % 2 != 0 and n in range(2,5):
#     #     print("not weird")            ----- WE can write this code without this step also

#     if n % 2 == 0 and n in range (6,21):
#         print("weird")

# else:
#     print("weird")


#####or


n = int(input())
if n % 2 == 0:
    if n in range(2,6):
        print("Not Weird")

    elif n in range(6,21):
        print("Weird")

    elif n > 20:
        print("Not Weird")
else:
    print("Weird")
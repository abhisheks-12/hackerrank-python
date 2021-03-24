n = int(input("Enter the num: "))
my_score = {}

for i in range(n):
    name , *line = input("Name: ").split()
    # print(name)
    # print(line)
    score = list(map(float,line))
    my_score[name] = score
query_name = input("enter the: ")

a  = my_score[query_name]

sum = 0
for i in a:
    sum = sum +i
    b = sum/3
print(format(b,".2f"))






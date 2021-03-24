# string = "abracadabra"
# # string = list(string)
# # string[5] = "k"
# # x = "".join(string)
# # print(type(x))
# # print(x)

# # another approach
# print(string[:5] + "k" + string[6:])


def mutate_string(s,i,c):
    return s[:i] + c + s[i+1:]
if __name__ == '__main__':
    s = input("Enter: ")
    i, c = input("Enter1: ").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)





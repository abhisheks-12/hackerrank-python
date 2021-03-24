# ABCDABC  ----- string
# BCD  ---- sub string

def count_substring(string,sub):
    c = 0
    l = len(sub)
   
    for i in range(len(string)):
        a = string[i: i+l]
        if a == sub:
            c = c + 1
    return c

string = input("Enter the string: ").strip()
sub = input("Enter: ").strip()
print(count_substring(string,sub))





    

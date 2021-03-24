l = []
def swap_case(s):
    result = " "
    for w in s:
        if w == w.lower():
            result = result + w.upper()
        elif w == w.upper():
            result = result + w.lower()

    return result
           
        

a = swap_case("aBHIU is MY")
print(a)







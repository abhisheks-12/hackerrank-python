# qA2

a = input('Enter The string: ')


print(any(c.isalnum() for c  in a))
print(any(c.isalpha() for c  in a))
print(any(c.isdigit() for c in a))
print(any(c.islower() for  c in a))
print(any(c.upper() for  c in a))
  # any is function of python which always return true

      

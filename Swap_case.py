#swapcase hacker rank problem

s = input()
def swap_case(s):
    word=' '
    for i in s:
       if i.islower():
          new=i.upper()
          word+=new
       elif i.isupper():
          new=i.lower()
          word+=new
    return word

result = swap_case(s)
print(result)

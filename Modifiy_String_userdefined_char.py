'''Modify a string with user defined character at user defined postition
    Note : String is immutable
'''
#Method 1
'''
string = input('enter string ')
position = int(input('enter position '))
char = input('enter char ')

strt = list(string)
a=strt.remove(strt[position])
strt.insert(position,char)
print(''.join(strt))
'''
#Method 2
#this given method without delete an existing character
'''
def mutate_string(string, position, character):
    String = list(string)
    String.insert(position,character)
    return ''.join(String)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
'''
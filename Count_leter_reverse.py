'''
    1.Read the string
    2.Read the letters count from reverse(number)
    3.print the characters
'''
#skill rack problesm 11
def repeat_alphabets(S, N):
    repeated_string = ""
    i = len(S) - 1
    while len(repeated_string) < N:
        repeated_string += S[i]
        i = (i - 1) % len(S)
    print(repeated_string[:N])

# Input
S = input().strip()
N = int(input().strip())

# Function call
repeat_alphabets(S, N)

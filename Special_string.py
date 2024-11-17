#Task
'''A string is called special if it can be written as the concatenation of two non-empty strings 's1' and 's2' such that 's1' contains all characters equal to 'a', and 's2' contains all characters equal to 'b'

You are provided with T test cases and for each test case, you are provided with string s. Your task is to find and print the number of special strings:

Note:

Each string contains only lowercase characters.

Input Format:

The input is given in the following format:

The first line contains T.

Each of the T subsequent lines contains string s.

The input will be read from the STDIN by the candidate

Output Format:

Print the number of special strings.

The output will be matched to the candidate's output printed on the STDOUT

Constraints:

1≤T≤100.

1 string length ≤ 5000.

Example:

Input:

4

ab

xyz

aab

axb

Output:

2

Explanation:

For the third test case, we can have s1= "aa" and s2- "b". Since the given strings are the concatenation of st and s2, where si contains all characters as 'a', and s2 contains all characters a 'b', and both s1 and s2 are non-empty, hence, this is a special string.

A similar explanation can be framed for the first test case as well, and those are the only two special strings in the given list of strings, and hence, the answer is 2.'''

#Solution
count = int(input('Enter count: '))
strings = []
total_s = []

for i in range(count):
    String = input('Enter a string: ')
    strings.append(String)

for word in strings:
    s1 = ''
    s2 = ''
    for char in word:
        if char == 'a':
            s1 += char
            print(s1)
        elif char == 'b':
            s2 += char
            print(s2)
        else:
            break

    combined = s1 + s2
    if combined:  # Only add non-empty combined strings
        total_s.append(combined)

# Remove unwanted elements using a list comprehension
total_s = [item for item in total_s if len(item) > 1]

# Print results
if total_s:  # Check if total_s is not empty
    print(len(total_s))  # Total number of elements
else:
    print("No valid strings found.")

'''Enter the number of students then followed buy a students name and theirs marks then find the percentage of the particular person'''
#find percentage HackerRank problem

if __name__ == '__main__':
    n = int(input('Enter the number of students : ')) #getting number of students
    student_marks = {} # students marks(ex : std1 23 34 54)
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    count=0
    name=student_marks[query_name]
    for i in name:
        count+=i
    result=(count)/(len(name))
    final="{:.2f}".format(result)#for fixing a point after a value like 20.00
    print(final)

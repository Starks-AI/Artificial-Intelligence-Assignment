from string import ascii_lowercase
import random
from itertools import combinations

print("Please enter the Number of clauses required ")
m = int(input())
print("Enter the number of variables in a clause ")
k = int(input())
print("Enter number of variables ")
n = int(input())

def makeProblem(m, k, n):
    pos_var = (list(ascii_lowercase))[:n]
    neg_var = [x.upper() for x in pos_var]
    variables = pos_var + neg_var
    t_hold = 10
    problems = []
    allCombos = list(combinations(variables, k))
    i = 0

    while i<t_hold:
        x = random.sample(allCombos, m)
        if x not in problems:
            i += 1
            problems.append(list(x))
            
    new_problems = []
    
    for x in problems:
        temp = []
        for sub in x:
            temp.append(list(sub))
        new_problems.append(temp)
    return problems

problems = makeProblem(m, k, n)


for i in range(len(problems)):
    print(problems[i])

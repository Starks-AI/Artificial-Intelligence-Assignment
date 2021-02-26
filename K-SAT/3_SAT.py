from string import ascii_lowercase
from itertools import combinations
import numpy as np
import random

print("Enter the number of clauses in the formula")
m = int(input())
print("Enter the number of literals in a clause ")
k = int(input())
print("Enter number of variables ")
n = int(input())

def makeProblem(m, k, n):
    pos_var = (list(ascii_lowercase))[:n]
    neg_var = [c.upper() for c in pos_var]
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
    return variables, problems

variables, problems = makeProblem(m, k, n)

#%%
def solve(problem, assign):
    count = 0
    for sub in problem:
        z = [assign[val] for val in sub]
        count += any(z)
    return count


def variableNeighbor(problem, assign, b, step):
    b_A = assign.copy()      
    assignValues = list(assign.values())
    assignKeys = list(assign.keys())
    steps = []
    poss_Assigns = []
    poss_Scores = []
    
    editAssign = assign.copy()
    
    initial = solve(problem, assign)
    if initial == len(problem):
        p = str(step) + "/" + str(step)
        return assign, p, b
    
    for i in range(len(assignValues)):
        step += 1
        editAssign[assignKeys[i]] = abs(assignValues[i]-1)
        c = solve(problem, editAssign)
        poss_Assigns.append(editAssign.copy())
        poss_Scores.append(c)
        steps.append(step)
    
    selected = list(np.argsort(poss_Scores))[-b:]
    
    if len(problem) in poss_Scores:
        index = [i for i in range(len(poss_Scores)) if poss_Scores[i]==len(problem)]
        p = str(steps[index[0]]) + "/" + str(steps[-1])
        return poss_Assigns[index[0]], p, b
    
    else:
        s_Assigns = [poss_Assigns[i] for i in selected]
        for a in s_Assigns:
            return variableNeighbor(problem, a, b+1, step)
        
        
def hillClimbing(problem, assign, parentNum, received, step):
    
    b_A = assign.copy()      
    a_Values = list(assign.values())
    a_Keys = list(assign.keys())
    
    maxNum = parentNum
    maxAssign = assign.copy()
    editAssign = assign.copy()
    
    for i in range(len(a_Values)):
        step += 1
        editAssign[a_Keys[i]] = abs(a_Values[i]-1)
        c = solve(problem, editAssign)
        if maxNum<c:
            received = step
            maxNum = c
            maxAssign = editAssign.copy()
            
    if maxNum==parentNum:
        s = str(received) + "/" + str(step-len(a_Values))
        return b_A, maxNum, s
    else:
        parentNum = maxNum
        bestassign = maxAssign.copy()
        return hillClimbing(problem, bestassign, parentNum, received, step)


def beamSearch(problem, assign,  b, stepSize):
    
    b_A = assign.copy()      
    a_Values = list(assign.values())
    a_Keys = list(assign.keys())
    steps = []
    p_Assigns = []
    p_Scores = []
    
    editAssign = assign.copy()
    
    initail = solve(problem, assign)
    if initial == len(problem):
        p = str(stepSize) + "/" + str(stepSize)
        return assign, p
    
    for i in range(len(a_Values)):
        stepSize += 1
        editAssign[a_Keys[i]] = abs(a_Values[i]-1)
        c = solve(problem, editAssign)
        p_Assigns.append(editAssign.copy())
        p_Scores.append(c)
        steps.append(stepSize)
    
    selected = list(np.argsort(p_Scores))[-b:]
    
    if len(problem) in p_Scores:
        index = [i for i in range(len(p_Scores)) if p_Scores[i]==len(problem)]
        p = str(steps[index[0]]) + "/" + str(steps[-1])
        return p_Assigns[ index[0] ], p
    else:
        s_Assigns = [p_Assigns[i] for i in selected]
        for a in s_Assigns:
            return beamSearch(problem, a, b, stepSize)


def assignment(variables, n):
    forPositive = list(np.random.choice(2,n))
    forNegative = [abs(1-i) for i in forPositive]
    assign = forPositive + forNegative
    var_assign = dict(zip(variables, assign))
    return var_assign

assign = assignment(variables, n)
#print(assign)
#print(problems[0])

h_Assigns = []
assigns = []
h_n = []
initials = []
hill_penetration = []
beam_penetration = []
var_penetration = []
v_n = []
b_var = []
b_n = []
bAssigns = []
vAssigns = []
i = 0


for problem in problems:
    i += 1
    l =[]
    assign = assignment(variables, n)
    initial = solve(problem, assign)
    b_A, score, hp = hillClimbing(problem, assign, initial, 1, 1)
    h_Assigns.append(b_A)
    assigns.append(assign)
    h_n.append(score)
    initials.append(initial)
    hill_penetration.append(hp)
    
    h3, b3s = beamSearch(problem, assign, 3, 1)
    bAssigns.append(h3)
    beam_penetration.append(b3s)
    
    h4, b4s = beamSearch(problem, assign, 4, 1)
    
    v, p, bb = variableNeighbor(problem, assign, 1, 1)
    var_penetration.append(p)
    b_var.append(bb)
    vAssigns.append(v)
    
    print('Problem ',i,': ',problem)
    print('HillClimbing: ',b_A,', Penetrance:', hp)
    print('Beam search (3): ',h3,', Penetrance:', b3s)
    print('Beam search (4): ', h4,', Penetrance:',b4s)
    print('Variable Neighbourhood: ',v,', Penetrance:',p)
    print()
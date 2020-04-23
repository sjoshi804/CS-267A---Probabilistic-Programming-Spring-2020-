import random
from copy import deepcopy

def evaluate(cnf):
    for clause in cnf:
        if True in clause:
            continue
        else:
            return False
    return True

def substitute(cnf, assignments):
    for clause_num in range(0, len(cnf)):
        for literal_num in range(0, len(cnf[clause_num])):
            if cnf[clause_num][literal_num] > 0:
                cnf[clause_num][literal_num] = assignments[cnf[clause_num][literal_num]]
            else:
                cnf[clause_num][literal_num] = (not assignments[-cnf[clause_num][literal_num]])
    return cnf

def sample(weights):
    assignments = {}
    for literal in weights:
        if random.random() < weights[literal]:
            assignments[literal] = True
        else:
            assignments[literal] = False
    return assignments

def estimate_probability(cnf, weights, num_trials):
    num_successes = 0
    for i in range(0, num_trials):
        if evaluate(substitute(deepcopy(cnf), sample(weights) )):
            num_successes += 1
    return (num_successes / num_trials)

# CNF 1: (a or b or ¬c)∧(b or c or d or ¬e)∧(¬b or ¬d or e)∧(¬a or ¬b) 
# Weights 1: Pr(a) = 0.3,Pr(b) = 0.6,Pr(c) = 0.1,Pr(d) = 0.8,Pr(e) = 0.4
cnf_1 = [[1, 2, -3], [2, 3, 4, -5], [-2, -4, 5], [-1, -2]]
weights_1 = {1: 0.3, 2: 0.6, 3: 0.1, 4: 0.8, 5: 0.4}
print("Testing CNF 1")
print("Trial 1: " + str(estimate_probability(cnf_1, weights_1, 1000)))
print("Trial 2: " + str(estimate_probability(cnf_1, weights_1, 1000)))
print("Trial 3: " + str(estimate_probability(cnf_1, weights_1, 1000)))

# CNF 2: (¬a or c or d) ∧ (b or c or ¬d or e) ∧ (¬c or d or ¬e)
# Weights 2: Pr(a) = 0.2,Pr(b) = 0.1,Pr(c) = 0.8,Pr(d) = 0.3,Pr(e) = 0.5
cnf_2 = [[-1, 3, 4], [2, 3, -4, 5], [-3, 4, -5]]
weights_2 = {1: 0.2, 2: 0.1, 3: 0.8, 4: 0.3, 5: 0.5}
print("Testing CNF 2")
print("Trial 1: " + str(estimate_probability(cnf_2, weights_2, 1000)))
print("Trial 2: " + str(estimate_probability(cnf_2, weights_2, 1000)))
print("Trial 3: " + str(estimate_probability(cnf_2, weights_2, 1000)))
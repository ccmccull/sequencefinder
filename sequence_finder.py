# Sequence Finder

import random

def CheckEquation(x): 
    return x[0] + 13 * x[1] / x[2] + x[3] + 12 * x[4] - x[5] - 11 + x[6] * x[7] / x[8] - 10 == 66

def AddSequenceIfNew(foundSequences, newSequence):
    if foundSequences.count(newSequence) == 0:
        foundSequences.append(newSequence)
    return(foundSequences)

a = range(1, 10)

print("start")

# The first sequence is just a placeholder so that AddSequenceIfNew
# will work on the first found sequence.
foundSequences = [[0, 0]]
numberFound = 0
while numberFound < 100:
    a = random.sample(a, 9)
    if CheckEquation(a):
        foundSequences = AddSequenceIfNew(foundSequences, a)
        numberFound = len(foundSequences) - 1
        print 'numberFound', numberFound

print 'Sequences:'
for i in range(1, len(foundSequences)):
    print i, foundSequences[i]

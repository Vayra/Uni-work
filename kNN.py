# INF4490 Oblig 2
# Simple Classifier
# k-nearest-neighbors
from numpy import *
###########
# knn, based on the implementation in "Machine Learning: An Algorithmic Perspective" by Marsland
# I chose to base my implementation on this because it's a very nice and simple implementation (if
# wrongly indented in the bcook). 
def knn(k, data, dataClass, inputs):
    nInputs = len(inputs)
    closest = zeros(nInputs)
    
    for n in range(nInputs):
        distances = sum((data - inputs[n,:])**2, axis = 1)
    
        #find nearest neighbors
        indices = argsort(distances, axis = 0)
        
        classes = unique(dataClass[indices[:k]])
        if len(classes) == 1:
            closest[n] = unique(classes)
        else:
            counts = zeros(max(classes) + 1)
            for i in range(k):
                counts[dataClass[indices[i]]] += 1
                closest[n] = max(counts)
    return closest
    
    
###########
# Input
input = open('EMG data\movements_day1.dat', 'r')
day1 = input.read()
day1 = day1.split('\n')
if len(day1[-1]) != len(day1[0]): day1 = day1[:-1] # if last line is empty remove it
for x in range(len(day1)):
    day1[x] = day1[x].split('\t')
    for y in range(len(day1[x])):
        day1[x][y] = float(day1[x][y])

input = open('EMG data\movements_day2.dat', 'r')
day2 = input.read()
day2 = day2.split('\n')
if len(day2[-1]) != len(day2[0]): day2 = day2[:-1]
for x in range(len(day2)):
    day2[x] = day2[x].split('\t')
    for y in range(len(day2[x])):
        day2[x][y] = float(day2[x][y])
        
input = open('EMG data\movements_day3.dat', 'r')
day3 = input.read()
day3 = day3.split('\n')
if len(day3[-1]) != len(day3[0]): day3 = day3[:-1]
for x in range(len(day3)):
    day3[x] = day3[x].split('\t')
    for y in range(len(day3[x])):
        day3[x][y] = float(day3[x][y])
        
input = open('EMG data\movements_day1-3.dat', 'r')
day13 = input.read()
day13 = day13.split('\n')
if len(day13[-1]) != len(day13[0]): day13 = day13[:-1]
for x in range(len(day13)):
    day13[x] = day13[x].split('\t')
    for y in range(len(day13[x])):
        day13[x][y] = float(day13[x][y])

classes = [x for x in range(9)] #1-8 with an empty class at 0
k = 5
data = [] # trained data goes here

for run in range(6):
    print("\n----------------------")
    print("Training on dataset:")
    if run in (0, 1): 
        train = day1
        print("day1")
    elif run in (2, 3):
        train = day2
        print("day2")
    else: 
        train = day3
        print("day3")
    
    print("\nValidating on: ")
    if run in (2,4): 
        validate = day1
        print("day1")
    elif run in (0, 5): 
        validate = day2
        print("day2")
    else: 
        validate = day3
        print("day3")
    for u in range(len(validate)):
        validate[u] = validate[u][:-1]
    validate = array(validate)
    # Train
    data = [train[x][:-1] for x in range(len(train))]
    data = array(data)
    closest = knn(k, data, classes, validate)
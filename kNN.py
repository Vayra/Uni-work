# INF4490 Oblig 2
# Simple Classifier
# k-nearest-neighbors
import numpy
###########
# knn, based on the implementation in "Machine Learning: An Algorithmic Perspective" by Marsland
# I chose to base my implementation on this because it's a very nice and simple implementation (if
# wrongly indented in the bcook). 
def knn_train(k, data, dataClass, inputs):
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
                counts[dataClass[indices[i]] += 1
                closest[n] = max(counts)
    return closest
    
    
###########
# Input
input = open('EMG data\movements_day1.dat', 'r')
day1 = input.read()
day1 = day1.split('\n')
if len(day1[-1]) != len(day1[0]): day1 = day1[:-1] # if last line is empty remove it

input = open('EMG data\movements_day2.dat', 'r')
day2 = input.read()
day2 = day2.split('\n')
if len(day2[-1]) != len(day2[0]): day2 = day2[:-1]

input = open('EMG data\movements_day3.dat', 'r')
day3 = input.read()
day3 = day3.split('\n')
if len(day3[-1]) != len(day3[0]): day3 = day3[:-1]
rc
input = open('EMG data\movements_day1-3.dat', 'r')
day13 = input.read()
day13 = day13.split('\n')
if len(day13[-1]) != len(day13[0]): day13 = day13[:-1]

for run in range(6):
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
    
    
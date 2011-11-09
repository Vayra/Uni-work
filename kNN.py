# INF4490 Oblig 2
# Simple Classifier
# k-nearest-neighbors

###########
# knn, based on the implementation in "Machine Learning: An Algorithmic Perspective" by Marsland
# 
def knn_train(k, data, dataClass, inputs):
    nInputs = len(inputs)
    closest = [0 for x in range(nInputs)]
    

    
    
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
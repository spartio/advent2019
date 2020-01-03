from imports.imports import operate, readFile
import itertools

file = file2 = readFile("input7")

sequence1 = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
sequence2 = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]
sequence3 = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32,
             31, 31, 4, 31, 99, 0, 0, 0]
sequence4 = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99,
             0, 0, 5]
sequence5 = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
             -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
             53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]

fullThruster = thruster = 0

# signal = ([0, 1, 2, 3, 4])
signal = ([1, 0, 4, 3, 2])
signals = []

for L in range(0, len(signal) + 1):
    for subset in itertools.permutations(signal, 5):
        # print(subset)
        signals.append(subset)

# print(signals)
# print(signals[0][0])
# operate(file, signal)

sigs = [[0, 1, 2, 3, 4], [1, 0, 4, 3, 2], [4, 3, 2, 1, 0]]
thrusters = []
for sig in signals:
    thruster = 0
    for x in sig:
        thruster = operate(file, x, thruster)
    thrusters.append(thruster)
print(max(thrusters))

sig5 = [9, 8, 7, 6, 5]
sig6 = [9, 7, 8, 5, 6]
thruster = 0
#for a in range(500):
for x in sig6:
    print(x)
    thruster = operate(sequence5, x, thruster)
    print(thruster)

# thruster=0
# for x in range(5):
#   thruster=operate(sequence2, x,thruster)
#  print(thruster)


# for x in signal:

# print(operate(sequence3, signal))
#   operate(sequence3, signal)

'''                                           
for x in signals:                           
   print(x)                                
   thruster = operate(file, x)             
   if thruster > fullThruster:             
     fullThruster = thruster             
                                          
print("full:{0}".format(fullThruster))      
                                        
    print(x)                                
    inputs = [x, thruster]                  
    thruster = operate(file, inputs)        
                                            
#print(signals)                             
#operate(sequence2, [0, 0])                 
'''

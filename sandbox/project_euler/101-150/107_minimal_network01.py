################################################################################
# 107_minimal_network.py
################################################################################
from time import time
import csv
from scipy.sparse.csgraph import minimum_spanning_tree 
import numpy as np
################################################################################
def process_file():
    filename = '107_network.txt'
    #filename = '107_example.txt'
    lst = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            one_row = [int(i) if i.isnumeric() else 0 for i in line]
            lst.append(one_row)
    return np.array(lst)
################################################################################
def weight_of_network(data):
    total = 0
    for row in range(len(data)):
        for col in range(len(data)):
            total += data[row][col]
    return total
################################################################################
def display_list(data):
    print('-------------------------')
    for row in data:
        print(row)
    print('-------------------------')
################################################################################
start = time()
start_data = process_file()
start_weight = weight_of_network(start_data)//2
print('Starting Network Weight:',start_weight)

tree = minimum_spanning_tree(start_data)

end_data = tree.toarray()
end_weight = weight_of_network(end_data)
print('Ending Network Weight..:',int(end_weight))

print('Maximum Saving.........:',int(start_weight-end_weight))
print('Run Time...............:',time()-start)
################################################################################
#solution: 259679
################################################################################

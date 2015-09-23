# Name: Steven Conflenti
# Email: stco8901@colorado.edu
# SUID: 103136126
#
import sys
import random
import time
import matplotlib 
import pylab

# --------- Insertion Sort -------------
# Implementation of getPosition
# Helper function for insertionSort
def getPosition(rList, elt):
    # Find the position where element occurs in the list
    #
    for (i,e) in enumerate(rList):
        if (e >= elt):
            return i
    return len(rList)

# Implementation of Insertion Sort 
def insertionSort(lst):
    n = len(lst)
    retList = []
    for i in lst:
        pos = getPosition(retList,i)
        retList.insert(pos,i)    
    return retList

#------ Merge Sort --------------
def mergeSort(lst):
    # TODO: Implement mergesort here
    # You can add additional utility functions to help you out.
    # But the function to do mergesort should be called mergeSort

	n = len(lst)
	if (n <= 1):
		return lst
	else:
		x = n/2
		l1 = mergeSort(lst[0:x])
		l2 = mergeSort(lst[x:n])
		return merge(l1, l2)
		
def merge(l1, l2):
	l3 = []
	i = 0
	j = 0
	
	while (i < len(l1) and j < len(l2)):
		if (l1[i] < l2[j]):
			l3.append(l1[i])
			i+=1
		elif (l1[i] >= l2[j]):
			l3.append(l2[j])
			j+=1
	if (i != len(l1)):
		while (i < len(l1)):
			l3.append(l1[i])
			i+=1
	elif (j != len(l2)):
		while (j < len(l2)):
			l3.append(l2[j])
			j+=1
	return l3

#------ Quick Sort --------------
def quickSort(lst):
    # TODO: Implement quicksort here
    # You may add additional utility functions to help you out.
    # But the function to do quicksort should be called quickSort

	n = len(lst)
	smaller, equal, bigger = [], [], []
    
	if(n <= 1):
		return lst
	
	else:
		piv = lst[0]
		for i in range(1, n):
			if lst[i] < piv:
				smaller.append(lst[i])
			if lst[i] == piv:
				equal.append(lst[i])
			if lst[i] > piv:
				bigger.append(lst[i])
		equal.append(lst[0])
		return quickSort(smaller) + equal + quickSort(bigger)
	

# ------ Timing Utility Functions ---------

# Function: generateRandomList
# Generate a list of n elements from 0 to n-1
# Shuffle these elements at random

def generateRandomList(n):
   # Generate a random shuffle of n elements
   lst = list(range(0,n))
   random.shuffle(lst)
   return lst


def measureRunningTimeComplexity(sortFunction,lst):
    t0 = time.clock()
    sortFunction(lst)
    t1 = time.clock() # A rather crude way to time the process.
    return (t1 - t0)


# --- TODO

# Write code to extract average/worst-case time complexity

def complexity(sortFunction):
	
	n = []
	averageTime = []
	worstTime = []
	i = 5
	total = 0
	worst = 0
	
	while(i <= 500):
		for j in range(0, 1000):
			lst = generateRandomList(i)
			t = measureRunningTimeComplexity(sortFunction, lst)
			total += t
			if(t > worst):
				worst = t
		average = total / 1000
		n.append(i)
		averageTime.append(average)
		worstTime.append(worst)
		worst = 0
		total = 0
		i += 5

	matplotlib.pyplot.scatter(n,averageTime, label='Average Case')
	matplotlib.pyplot.scatter(n,worstTime,c='red',label='Worst Case')
	matplotlib.pyplot.ylabel('Run Time (s)')
	matplotlib.pyplot.xlabel('Number of Elements (n)')
	if(sortFunction == quickSort):
		matplotlib.pyplot.title('Quicksort Average vs. Worst Case Complexity')
	elif(sortFunction == mergeSort):
		matplotlib.pyplot.title('Mergesort Average vs. Worst Case Complexity')
	elif(sortFunction == insertionSort):
		matplotlib.pyplot.title('Insertion Sort Average vs. Worst Case Complexity')
	matplotlib.pyplot.show()
	

def main():
	complexity(quickSort)
	complexity(mergeSort)
	complexity(insertionSort)
	
if __name__ == "__main__":
    main()

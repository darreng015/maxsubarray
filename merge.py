import random
import math
import matplotlib.pyplot as plt
import numpy 

counter = 0

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    global counter
    if not left or not right:  # Count comparisons when checking for empty subarrays
        # counter += 1
        return left or right

    if left[0] < right[0]:
        counter += 1  # Count element comparison
        return [left[0]] + merge(left[1:], right)
    counter += 1  # Count element comparison
    return [right[0]] + merge(left, right[1:])






N_values = []
comparison_counts = []
worst_case_counts = [] # N * math.log2(N)
counter_array =[]



def generate_array(N):
    newArray =list(range(1, N + 1))
    random.shuffle(newArray)
    return newArray


x = int(input("Enter number of elements: "))
print("Enter ",x, " numbers in ascending order\n")
for i in range(0,x):
    N = int(input("\nEnter array size: "))
    N_values.append(N)
    arr = generate_array(N)
    n = len(arr)
    print("\nGiven array is")
    for i in range(n):
        print(arr[i],end=" ")
          

    arr = merge_sort(arr)
    comparison_counts.append(counter)
    worst_case_counts.append(int(N * math.log2(N)))
    print("\n\nSorted array is")
    for i in range(n):
        print(arr[i],end=" ")
    print("\n")


	
print("\nCounter=", counter)
print("\n================================================================================================================")

newarray=numpy.copy(comparison_counts)
for i in range(1,len(comparison_counts)):
     comparison_counts[i]=newarray[i]-newarray[i-1]
    

# Printing the table for N, Actual comparison count, worst case comparison count
print("\n"f"{'N':<5}{'Actual Count':<15}{'Worst Case T(N)':<15}")
for N, comparison_count, worst_case_count in zip(N_values, comparison_counts, worst_case_counts):
    print(f"{N:<10}{comparison_count:<15}{worst_case_count:<15}")

# Plotting graph
plt.plot(N_values, comparison_counts, label='Actual Count')
plt.scatter(N_values, comparison_counts)
plt.plot(N_values, worst_case_counts, label='Worst Case Count', linestyle='dashdot')
plt.scatter(N_values, worst_case_counts)
plt.xlabel('N (Array Size)')
plt.ylabel('Count of Comparisons')
plt.legend()
plt.title('Merge Sort Complexity Analysis')
plt.grid(True)
plt.show()


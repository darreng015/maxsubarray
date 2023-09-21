import random
import matplotlib.pyplot as plt

# Insertion Sort
def insertion_sort(arr):
    comparisonsCount = 0
    for i in range(1, len(arr)):
        element = arr[i]
        j = i - 1
        while j >= 0 and element < arr[j]:
            comparisonsCount += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = element
    return arr, comparisonsCount

# Generate array of N elements in random order
def generate_array(N):
    newArray =list(range(1, N + 1))
    random.shuffle(newArray)
    return newArray


# Arrays to store results
N_values = []
comparison_counts = []
worst_case_counts = []

x = int(input("Enter number of arrays: "))
print("Enter ",x, " numbers in ascending order\n")
for i in range(0,x):
    N = int(input("\nEnter array size: "))
    N_values.append(N)
    arr = generate_array(N)
    n = len(arr)
    print("\nGiven array is")
    for i in range(n):
        print(arr[i],end=" ")
          

    arr, counter = insertion_sort(arr)
    comparison_counts.append(counter)
    worst_case_counts.append(int(((N * N )-N)/2))
    print("\n\nSorted array is")
    for i in range(n):
        print(arr[i],end=" ")

    print("\ncomparisons : ", counter)


# Display the table
print("\n"f"{'N':<5}{'Actual Count':<15}{'Worst Case T(N)':<15}")
for N, comparison_count, worst_case_count in zip(N_values, comparison_counts, worst_case_counts):
    print(f"{N:<10}{comparison_count:<15}{worst_case_count:<15}")

# Plot the results
plt.plot(N_values, comparison_counts, label='Actual Count')
plt.scatter(N_values, comparison_counts)
plt.plot(N_values, worst_case_counts, label='Worst Case Count', linestyle='--')
plt.scatter(N_values, worst_case_counts)
plt.xlabel('N (Array Size)')
plt.ylabel('Count of Comparisons')
plt.legend()
plt.title('Insertion Sort Complexity Analysis')
plt.grid(True)
plt.show()

import random

def SubarrayWithMaxSum(nums):
	
# Initialize currMax and globalMax
# with first value of nums
	currMax = nums[0]
	globalMax = nums[0]

# Iterate for all the elements
# of the array
	for i in range(1, len(nums)):

# Update currMax
		currMax = max(nums[i], nums[i] + currMax)

# Check if currMax is greater
# than globalMax
		if (currMax > globalMax):
			globalMax = currMax
			endIndex = i

	startIndex = endIndex

# Traverse in left direction to
# find start Index of subarray
	while (startIndex >= 0):
		globalMax -= nums[startIndex]

		if (globalMax == 0):
			break

	# Decrement the start index
		startIndex -= 1

	# Printing the elements of
	# subarray with max sum
	sum=0
	print("\n\nSub array = ")
	for i in range(startIndex, endIndex + 1):
		sum +=nums[i]
		print(nums[i], end = " ")
	print("\nSum = ", sum)
	





def generate_array(N):
    newArray =random.sample(range(-N*2, N*2), N)
    random.shuffle(newArray)
    return newArray

x = int(input("Enter number of arrays: "))
print("Enter ",x, " numbers in ascending order\n")
for i in range(0,x):
    N = int(input("\n-------------------------------\nEnter array size: "))
    arr = generate_array(N)
    n = len(arr)
    print("\nGiven array is")
    for i in range(n):
        print(arr[i],end=" ")
          

    arr=SubarrayWithMaxSum(arr)




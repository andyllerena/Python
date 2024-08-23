#### Basic Implementation of Binary Search ####
#### Time Complexity of Binary Search = Olog(n) ####

def binarySearch(arr,target):

    left = 0 
    right = len(arr) - 1 

    while left <= right:
        
        mid = (left + right) // 2

        if arr[mid]== target:
            return mid
        
        elif arr[mid] > target:
            right = mid - 1

        else:
            left = mid + 1
    
    return -1


# print(f"The target: {target} was found at index {binarySearch(arr,target)}")



#### First and Last Occurence using Binary Search ####
def firstAndLastBinarySearch(arr, target, leftBias):
    left = 0
    right = len(arr) - 1
    i = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            i = mid
            if leftBias:
                right = mid - 1  # Continue searching on the left side
            else:
                left = mid + 1  # Continue searching on the right side
    return i
   

arr = [2, 3, 45, 63, 4, 52, 1, 4, 56, 3, 7, 8, 6, 9]
target = 100

arr.sort()
# print(f"Sorted Array: {arr}")

left = firstAndLastBinarySearch(arr,target,True)
right = firstAndLastBinarySearch(arr,target,False)

# print([left, right])


#### Search in rotated sorted array using Binary Search ####
def searchRotatedArrayBinarySearch(arr, target):

    left = 0 
    right = len(arr) - 1 

    while left <= right:

        mid = (left + right) // 2

        if target == arr[mid]:
            return mid
        
        if arr[left] <= arr[mid]:
            if target < arr[left] or target > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
            
        else:
            if target > arr[right] or target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1
arr = [4, 5, 6, 7, 0, 1, 2]
target = 2

# print(arr)
# print(f"The target {target} was found at index {searchRotatedArrayBinarySearch(arr,target)}")

#### Search Insert Position using Binary Search ####
def searchInsertBinarySearch(arr,target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2
        
        if target == arr[mid]:
            return mid
        
        elif target < arr[mid]:
            right = mid - 1
        
        else:
            left = mid + 1
    return left 


# arr = [2, 3, 45, 63, 4, 52, 1, 4, 56, 3, 7, 8, 6, 9]
# target = 4

# arr.sort()
# print(f"Sorted Array: {arr}")
# print(searchInsertBinarySearch(arr,target))


#### 2D Matrix using Binary Search ####
def searchMatrix(matrix, target):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    top = 0 
    bottom = ROWS - 1

    while top <= bottom:
        row = (top + bottom) // 2

        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            break
    
    if not (top <= bottom):
        return False
    
    row = (top + bottom) // 2
    left = 0 
    right = COLS - 1

    while left <= right:
        mid = (left + right) // 2
        if target > matrix[row][mid]:
            left = mid + 1
        elif target < matrix[row][mid]:
            right = mid - 1
        else:
            return True
    
    return False

# Example usage:
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

# target = 3

# result = searchMatrix(matrix, target)
# print(f"Target {target} found in matrix: {result}")

# # Trying with a target that is not in the matrix
# target = 13
# result = searchMatrix(matrix, target)
# print(f"Target {target} found in matrix: {result}")

#### Find Minimum in Rotated Sorted Array####

def findMin(nums):
    res = nums[0]
    left = 0 
    right = len(nums) - 1

    while left <= right:
        # Early exit: If the subarray is already sorted, return the minimum.
        if nums[left] < nums[right]:
            res = min(res, nums[left])
            break

        mid = (left + right) // 2
        res = min(res, nums[mid])

        # If the left side is sorted, the minimum is on the right side.
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1

    return res

nums = [4, 5, 6, 7, 0, 1, 2]

print(nums)
print(f"Min Value: {findMin(nums)}")


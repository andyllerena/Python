from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    prevMap = {}  # Dictionary to store previously seen numbers and their indices

    for i, n in enumerate(nums):
        diff = target - n  # Calculate the difference needed to reach the target
        print(f"Index: {i}, Number: {n}, Difference needed: {diff}, Previous Map: {prevMap}")

        if diff in prevMap:  # Check if the difference is already in the map
            print(f"Found! {diff} is in prevMap, returning indices: [{prevMap[diff]}, {i}]")
            return [prevMap[diff], i]  # Return the indices of the two numbers

        prevMap[n] = i  # Add the current number and its index to the map
        print(f"Updated Previous Map: {prevMap}\n")

    print("No two numbers add up to the target.")
    return []

# Example array to iterate many times
nums = [3,2,4,5]
target = 9
print(twoSum(nums, target))

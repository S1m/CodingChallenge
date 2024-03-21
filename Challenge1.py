'''
Challenge 1 - Zero Sum Game

Problem Statement:

You are given a list of integers. Going from left to right, your task is to write a function that returns the two numbers that sum to zero. 
If there are multiple pairs that sum to zero, return the pair with the smallest 
non-negative element. If all pairs start with a negative element, 
return the pair with the largest negative element.
If there are no elements that sum to zero, return an empty list.

Your function should have the following signature:
def find_zero_sum(nums: List[int]) -> List[int]:

Input:

The input nums is a list of integers (-10^3 <= nums[i] <= 10^3). 
The length of the list 1 <= len(nums) <= 10^3.

Output:

The function should return a list of two integers that sum to zero, or empty.

# Example test cases
#assert find_zero_sum([3, -4, -3, 4, 2, -2]), [2, -2]
#assert find_zero_sum([1, 2, 3]), []
#assert find_zero_sum([-2, 2, -3, 3, -4, 4]) == [-4, 4]

In the first example, there are two pairs that sum to zero: [-4, 4] and [2,-2]. 
The pair with the smallest non-negative element is [2, -2].

In the second example, there are no pairs that sum to zero, 
so the function returns an empty list.

In the third example, there are three pairs that sum to zero: [-2, 2], [-3, 3], and [-4, 4].
The pair with the largest negative element is [-4, 4].

Evaluation:

You will be evaluated on the correctness of your solution and its quality.
'''

def find_zero_sum(nums):

    # Write an O(n**2) solution
    # Possible pairs
    pairs = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == 0:
                pairs.append([nums[i], nums[j]])

    # Find the solution
    solution = []
    if len(pairs) == 0: # Look if no pairs
        pass # Do nothing as solution is already an empty list
    else:
        # Look for the smallest non-negative element
        small = 1001
        for pair in pairs:
            if pair[0] >= 0 and pair[0] < small:
                small = pair[0]
                solution = pair
        if len(solution) == 0: # If no non-negative element
            # Look for the largest negative element
            sortedPairs = sorted(pairs, key=lambda x: x[0])
            solution = sortedPairs[0]

    return solution # Replace this with your implementation
    
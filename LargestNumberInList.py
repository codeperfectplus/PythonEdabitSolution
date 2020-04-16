""" Create a function that takes a list of numbers. Return the largest number in the list.

Examples
findLargestNum([4, 5, 1, 3]) ➞ 5

findLargestNum([300, 200, 600, 150]) ➞ 600

findLargestNum([1000, 1001, 857, 1]) ➞ 1001 """

def findLargestNum( list ):
    max = list[ 0 ]
    for num in list:
        if num > max:
            max = num
    return max

LargestNum = findLargestNum([300, 200, 600, 150])
print(LargestNum)

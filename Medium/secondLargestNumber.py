def findSecondLargestNum(arr:list):
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    secondlargest = 0
    for num in arr:
        if num > secondlargest and num < max:
            secondlargest = num
    return secondlargest

arr = [2,3,5,6,6]
answer = findSecondLargestNum(arr)
print(answer)

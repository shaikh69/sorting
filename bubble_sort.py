arr = [-9, -2, 0, 11, 45]

for i in range(len(arr)):
    swapped = False
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
    if not swapped:
        break

print(arr)

# Questions that comes to my mind
# 1. why we need first loop if we just checking number is greater or not with j only
# ans: it is because it is for loop and when i reach to last number it was autometically sorted
# there is the actual logic in second loop you start with 1st element then go till before last element.
# swapped variable is for optimization if there is no swap at first then program breaks.
# 2. why we need to check j+1
# ans: because we are comparing two elements at a time and if we reach to last element then there is no j+1
# 3. why we need to check len(arr)-i-1
# ans: because we are already sorted the last i elements so we don't need to check them again.
# 4. why we need to check j < len(arr)-i-1
# ans: because we are already sorted the last i elements so we don't need to check them again.
# 5. why we need to check j+1 < len(arr)
# ans: because we are comparing two elements at a time and if we reach to last element then there is no j+1
# 6. why we need to check arr[j] > arr[j+1]
# ans: because we are sorting the array in ascending order and if arr[j] > arr[j+1] then we need to swap them.
# 7. why we need to check arr[j] < arr[j+1]
# ans: because we are sorting the array in descending order and if arr[j] < arr[j+1] then we need to swap them.


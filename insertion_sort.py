def insertion_sort(array):
    # there is the concept of left and right at first left is always sorted left = sorted right = unsorted
    for i in range(1, len(array)):
        j = i
        while array[j-1] >= array[j] and j > 0:
            #  here above you check if the cureent point element is greater than or equal to left element and at same time j should not be = 0 
            #  if the condition is true then swap the elements
            #  this is the main part of the insertion sort
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1
    return array

arr = [2,6,5,1,3,4]
print(insertion_sort(arr))
arr = [-2, -9, 0, 45, 11]
size = len(arr)

def selection_sort(arr, size):
    for i in range(size):
        min_ind = i
        
        for j in range(i+1, size):
            if arr[j] > arr[min_ind]:
                min_ind = j
            
        arr[j], arr[min_ind] = arr[min_ind], arr[j]
        
    return arr
    
print(selection_sort(arr,size))

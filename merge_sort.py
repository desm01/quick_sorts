
def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2

        left = array[:middle]

        right = array[middle:]

        merge_sort(left)

        merge_sort(right)

        i = 0 
        j = 0 
        k = 0

        while i < len (left) and j < len(right):
            if left[i] < right[j]:
            
                array[k] = left[i]
                i = i + 1

            else:
                array[k] = right[j]
                j = j + 1
        
            k = k + 1
    
        while i < len(left):
            array[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            array[k] = right[j]
            j = j + 1
            k = k + 1

array = [10,12,4,5,2,1,199,21,32,1,90,18]
merge_sort(array)

for item in array:
    print(item)

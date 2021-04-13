def insertion_sort(array):
    
    length_of_array = len(array)

    for i in range(1, length_of_array):
        currentElement = array[i]

        j = i - 1
        
        #   Shift elements that are greater than currentElement up once
        
        while (j >= 0 and array[j] > currentElement):
            
            array[j+1] = array[j]

            j = j -1

        array[j + 1] = currentElement 

    return array


array = [10,12,4,5,2,1,199,21,32,1,90,18]

insertion_sort(array)

for item in array:
    print(item)
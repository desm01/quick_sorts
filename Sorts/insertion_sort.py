

def insertion_sort(array):
    array_length = len(array)

    for i in range(1, array_length):

        currentElement = array[i]

        j = i -1

        while j >= 0 and array[j] >= currentElement:
            array[j+1] = array[j]
            j = j -1

        array[j + 1] = currentElement

    return array

def start_insertion_sort(array):
    insertion_sort(array)
    return array


def array_is_sorted(array):
    array_is_sorted = False
    array_length = len(array) - 1

    for i in range(0, array_length):
        if (array[i] > array[i+1]):
            return  False

    return True

def bubble_sort(array):
    array_length = len(array) - 1

    for i in range(0, array_length):
        if array[i] > array[i + 1]:
            value_one = array[i]
            value_two = array[i+1]

            array[i+1] = value_one
            array[i] = value_two

    if (array_is_sorted(array)):
        return
    else:
        bubble_sort(array)


def start_bubbble_sort(array):
    bubble_sort(array)
    return array

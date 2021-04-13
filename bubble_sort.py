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

array = [10,12,4,5,2,1,199,21,32,1,90,18]

bubble_sort(array)

for item in array:
    print(item)
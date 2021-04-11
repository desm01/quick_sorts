def quick_sort(array, low, high):
    if len(array) == 1:
        return array

    if low < high:
        pivot_point = partition(array, low, high)

        quick_sort(array, low, pivot_point - 1)
        quick_sort(array, pivot_point + 1, high)


def partition(array, low, high):
    index = low - 1
    pivot_point = array[high]

    for i in range(low, high):
        if array[i] <= pivot_point:

            index = index + 1

            array[index], array[i] = array[i], array[index]
            
    array[index + 1], array[high] = array[high], array[index + 1]
    return (index+1)



array = [10,12,4,5,2,1,199,21,32,1,90,18]

length = len(array) - 1
quick_sort(array, 0, length)

print("The Sorted Array is:")

for item in array:
	print(item)




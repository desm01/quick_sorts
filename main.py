from Sorts.bubble_sort import start_bubbble_sort
from Sorts.insertion_sort import insertion_sort, start_insertion_sort
from Sorts.merge_sort import merge_sort, start_merge_sort
from Sorts.quick_sort import quick_sort, start_quick_sort

from time import time

import sys

from random import randrange

sys.setrecursionlimit(15000)

def generate_array():
    array = []
    for i in range (0, 15000):
        number = randrange(100000)
        array.append(number)
    return array

array = generate_array()

def bubble_sort():
    print("Starting Bubble Sort")
    bubble_array = array.copy()

    bubble_sort_time = time()
    start_bubbble_sort(bubble_array)
    final_time = time()

    print("It took Bubble Sort: " + str(final_time - bubble_sort_time) + " seconds" + "\n\n\n\n")

def insertion_sort():
    print("Starting Insertion Sort")
    insertion_array = array.copy()
    
    insertion_sort_start = time()
    start_insertion_sort(insertion_array)
    insertion_sort_finish = time()

    print("It took Insertion Sort: " + str(insertion_sort_finish - insertion_sort_start) + "\n\n\n\n")

def quick_sort():
    print("Starting Quick Sort")
    quick_sort_array = array.copy()

    quick_sort_start = time()
    start_quick_sort(quick_sort_array)
    quick_sort_finish = time()


    print("It took Quick Sort: " + str(quick_sort_finish - quick_sort_start) + "\n\n\n\n")

def merge_sort():
    print("Starting Merge Sort")
    merge_sort_array = array.copy()

    merge_sort_start = time()
    start_merge_sort(merge_sort_array)
    merge_sort_finish = time()

    print("It took Merge Sort: " + str(merge_sort_finish - merge_sort_start) + "\n\n\n\n" )

merge_sort()
quick_sort()
bubble_sort()
insertion_sort()
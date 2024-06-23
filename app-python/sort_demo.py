from flask import Blueprint, render_template, current_app, request
from demo_data import create_search_data
from random import randint, shuffle
import time

sort_demo = Blueprint('sort_demo', __name__)

# Route to sort performance comparison
@sort_demo.route('/sort_demo')
def sorting_demo():
    result_times = []
    demo_data = create_search_data()
    shuffle(demo_data) #Randomized list of 100k data
    print(f'Demo data length: {len(demo_data)}')
    
    # Make copy of data for each sort function
    # To be sure all start with the same data
    
    # Timsort
    data_copy = demo_data[:]
    result_times.append(measure_time(timsort, data_copy))

    # Merge sort
    data_copy = demo_data[:]
    result_times.append(measure_time(merge_sort, data_copy))

    #Pivot sort
    data_copy = demo_data[:]
    result_times.append(measure_time(pivot_sort, data_copy))

    return render_template('sort_demo.html', result_times=result_times)

#Python built-in timsort function
def timsort(data):
    data.sort(key=lambda data: data.id)


#Merge Sort
def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i].id < right_half[j].id:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

#Pivot Sort
def pivot_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2].id
    left = [x for x in data if x.id < pivot]
    middle = [x for x in data if x.id == pivot]
    right = [x for x in data if x.id > pivot]
    return pivot_sort(left) + middle + pivot_sort(right)

#Measure time of sort function
def measure_time(sort_func, data):
    start_time = time.time()
    sort_func(data)
    end_time = time.time()
    return end_time - start_time



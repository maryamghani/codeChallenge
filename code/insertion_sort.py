"""
Insertion Sort array
"""


def insertion_sort_first_approach(array):
    for i in range(1, len(array)):
        for j in range(i):
            if array[i] < array[j]:
                current = array[i]
                array[i] = array[j]
                array[j] = current


def insertion_sort_second_approach(array):
    for i in range(1, len(array)):
        current_index = array[i]
        j = i - 1
        while j >= 0 and current_index < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = current_index

<<<<<<< HEAD:insertion_sort.py

if __name__ == '__main__':
    input_test = [12, 11, 13, 5, 6]
    insertion_sort_second_approach(input_test)
=======
>>>>>>> 63206c233c599edcf9e30a7334307ea849c170c9:code/insertion_sort.py

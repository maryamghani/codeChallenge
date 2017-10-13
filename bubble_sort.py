def bubble_sort(array):
    for x in range(0, len(array) - 1):
        for j in range (x+1 , len(array)):
            if array[x] > array[j]:
                bigger = array[x]
                array[x] = array[j]
                array[j] = bigger
    return array


def test_bubble_sort():
    array1 = [5, 1, 4, 2, 8]
    sorted_array = bubble_sort(array1)
    assert sorted_array == array1


def test_bubble_sort_with_replica():
    array1 = [5, 1, 1, 2, 8]
    sorted_array = bubble_sort(array1)
    assert sorted_array == array1


def test_bubble_sort_with_all_same_input():
    array1 = [1, 1, 1]
    sorted_array = bubble_sort(array1)
    assert sorted_array == array1
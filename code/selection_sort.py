def selection_sort(array):

    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == '__main__':
    input_test = [12, 11, 13, 5, 6]
    sorted_array = selection_sort(input_test)
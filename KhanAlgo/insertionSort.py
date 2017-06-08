def insert(array, rightIndex, value):
    j = rightIndex

    for elem in array:
        if value < array[j] and j >=0:
            array[j + 1] = array [j]; 
            j = j - 1
        else:
            array[j+1] = value
            return array


def insertionSort(array):
    if len(array) >=2:
        i = 1;
        for elem in array:
            print "i ", i, "array[i] ", array[i], "array", array 
            insert(array, i-1, array[i])
            i = i + 1
            if i > len(array)-1:
                return array
    return array





a = [3, 5, 7, 11, 13, 2, 9, 6]
print insertionSort(a)
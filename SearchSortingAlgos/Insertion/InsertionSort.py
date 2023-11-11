
def insertionSort(arr):

    #will consider the first elem as sorted
    for i in range(1, len(arr)):
        anchor = arr[i]
        j = i - 1

        #compare the anchor to the previously sorted elems
        while j>=0 and anchor < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        #if elems are less then push left till no longer true
        arr[j+1] = anchor #finally place anchor in the right spot
    return arr

if __name__ == '__main__':
    arr = [11,9,29,7,2,15,28]
    insertionSort(arr)
    print(arr)
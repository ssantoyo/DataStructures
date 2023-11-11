'''
Compute the running median of a sequence of numbers. 
That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers in a sorted list.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
'''

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


def running_median(arr):

    sorted_list =[]

    for num in arr:

        sorted_list.append(num)
        insertionSort(sorted_list)

        N = len(sorted_list)
        if N % 2 == 0: #even sorted list choose the two center idx
            median = (sorted_list[N // 2 - 1] + sorted_list[N // 2]) /2
        else: #chooses the middle idx
            median = sorted_list[N//2]

        print(median)

arr = [2,1,5,7,2,0,5]
running_median(arr)

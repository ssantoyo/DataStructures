# implementation of quick sort in python using hoare partition scheme
'''
// Sorts a (portion of an) array, divides it into partitions, then sorts those
algorithm quicksort(A, lo, hi) is 
  // Ensure indices are in correct order
  if lo >= hi || lo < 0 then 
    return
    
  // Partition array and get the pivot index
  p := partition(A, lo, hi) 
      
  // Sort the two partitions
  quicksort(A, lo, p - 1) // Left side of pivot
  quicksort(A, p + 1, hi) // Right side of pivot

// Divides array into two partitions
algorithm partition(A, lo, hi) is 
  pivot := A[hi] // Choose the last element as the pivot

  // Temporary pivot index
  i := lo - 1

  for j := lo to hi - 1 do 
    // If the current element is less than or equal to the pivot
    if A[j] <= pivot then 
      // Move the temporary pivot index forward
      i := i + 1
      // Swap the current element with the element at the temporary pivot index
      swap A[i] with A[j]

  // Move the pivot element to the correct pivot position (between the smaller and larger elements)
  i := i + 1
  swap A[i] with A[hi]
  return i // the pivot index
'''


#lumoto Impl.

def swap(arr, a, b):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]
    return arr

def parition(arr, lo, hi):
    pivot = arr[hi] #pivot is set to last element
    curr = 0
    #temp pivot index
    i = lo - 1

    for j in range(lo, hi):
        curr = arr[j]
        if curr <= pivot:
            i+=1
            swap(arr, i, j)
    i+=1
    swap(arr,i, hi)
    return i


def quickSort(arr, lo, hi):
    if lo >= hi or lo < 0:
        return
    pi = parition(arr, lo, hi)
    quickSort(arr, lo, pi - 1)
    quickSort(arr, pi +1, hi)




#Hoares Implementation
# def swap(a, b, arr):
#     if a!=b:
#         tmp = arr[a]
#         arr[a] = arr[b]
#         arr[b] = tmp

# def quick_sort(elements, start, end):
#     if start < end:
#         pi = partition(elements, start, end)
#         quick_sort(elements, start, pi-1)
#         quick_sort(elements, pi+1, end)

# def partition(elements, start, end):
#     pivot_index = start
#     pivot = elements[pivot_index]

#     while start < end:
#         while start < len(elements) and elements[start] <= pivot:
#             start+=1

#         while elements[end] > pivot:
#             end-=1

#         if start < end:
#             swap(start, end, elements)

#     swap(pivot_index, end, elements)

#     return end


if __name__ == '__main__':

    tests = [
        # [11,9,29,7,2,15,28],
        # [3, 7, 9, 11],
        [25, 22, 21, 10],
        # [29, 15, 28],
        # [],
        # [6]
    ]

    for elements in tests:
        quickSort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')


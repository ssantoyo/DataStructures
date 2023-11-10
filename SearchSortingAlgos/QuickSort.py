def swap(a,b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]
    return arr


def partition(elems, start, end):
    pivot_idx = start
    pivot = elems[pivot_idx]

    while start < end:
        while start < len(elems) and elems[start] <= pivot:
            start+=1

        while elems[end] > pivot:
            end-=1
        
        if start < end:
            swap(start, end, elems)
    
    swap(pivot_idx, end, elems)
    
    return end

def QuickSort(elems, start, end):
  if start < end:
    pi = partition(elems, start, end)
    QuickSort(elems, start, pi-1)
    QuickSort(elems, pi+1, end)


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    N = len(elements)
    QuickSort(elements, 0, N-1)
    print(elements)
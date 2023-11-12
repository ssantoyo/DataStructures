# def find_min_element(arr):
#     minVal = arr[0]
#     for i in range(len(arr)):
#         if  arr[i] < minVal :
#             minVal = arr[i]

#     return minVal
        


def selection_sort(arr):
    N = len(arr)
    for i in range(N-1): #if the rest are sorted up to the last elem, then no need to reach end
        min_idx = i
        for j in range(min_idx+1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        #optimization for first element if it is already sorted
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == '__main__':
    elements = [78,12,15, 8, 61, 53, 23, 27]
    selection_sort(elements)
    print(elements)

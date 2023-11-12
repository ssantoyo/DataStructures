from pprint import pprint
'''
Exercise can be found here: https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/5_MergeSort/merge_sort_exercise.md
'''


def merge_sort(arr, key=None, descending=None):
    if len(arr) <= 1:
        return
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left, key, descending)
    merge_sort(right, key, descending)

    merge_two_sorted_list(left, right, arr,key, descending)


def merge_two_sorted_list(left, right, arr, key, descending):
    len_left = len(left)
    len_right = len(right)

    i = j = k = 0

    if descending:
        while i < len_left and j < len_right:
            if left[i][key] >= right[j][key]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1

        while i < len_left:
            arr[k] = left[i]
            i+=1
            k+=1
        while j < len_right:
            arr[k] = right[j]
            j+=1
            k+=1
    else:
        while i < len_left and j < len_right:
            if left[i][key] <= right[j][key]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1

        while i < len_left:
            arr[k] = left[i]
            i+=1
            k+=1
        while j < len_right:
            arr[k] = right[j]
            j+=1
            k+=1

    return arr



if __name__ == '__main__':
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    
    merge_sort(elements, key="time_hours", descending=True)
    pprint(elements)
    print()
    merge_sort(elements, key="time_hours", descending=False)
    pprint(elements)
    # merge_sort(elements, key="name")
    # print()
    # pprint(elements)
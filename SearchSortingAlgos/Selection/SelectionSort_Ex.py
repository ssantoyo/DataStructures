
from pprint import pprint


def selection_sort(arr, keyA=None):
    N = len(arr)
    for i in range(N-1): #if the rest are sorted up to the last elem, then no need to reach end
        min_idx = i
        for j in range(min_idx+1, N):
            if arr[j][keyA] < arr[min_idx][keyA]:
                min_idx = j
        #optimization for first element if it is already sorted
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__=='__main__':
    names = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]
selection_sort(names, keyA="First Name")
pprint(names)
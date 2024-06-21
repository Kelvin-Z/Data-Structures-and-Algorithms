swap = 0


def mergesort(arr):
    global swap
    if len(arr) > 1:
        mid = len(arr)//2

        L = arr[:mid]   # Dividing the array elements
        R = arr[mid:]   # Into 2 halves

        mergesort(L)    # Sorting the first half
        mergesort(R)    # Sorting the second half

        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                swap += len(L)-i
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


while True:
    n = int(input())
    if n == 0:
        break
    ar = []
    swap = 0
    for i in range(n):
        ar.append(int(input()))
    mergesort(ar)
    print(swap)

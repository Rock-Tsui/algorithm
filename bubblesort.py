def bubble_sort(L):
    length = len(L)
    for i in range(length-1):
        for j in range(length-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    print(L)

if __name__ == '__main__':
    L = [34, 1, 11, 8, 13, 7, 20, 3, 5]
    bubble_sort(L)

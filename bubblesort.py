def sorted(L):
    length = len(L)
    for i in range(length):
        for j in range(i+1,length):
            if L[i] > L[j]:
                L[i] += L[j]
                L[j] = L[i] - L[j]
                L[i] -= L[j]
    print(L)

if __name__ == '__main__':
    L = [34,1,11,8,13,7,20,3,5]
    sorted(L)
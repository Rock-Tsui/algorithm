# Python3 program for finding the maximum number
# of trailing zeros in the product of the 
# selected subset of size k.
'''
Input : arr = {50, 4, 20}
        k = 2
Output : 3
Here, we have 3 subsets of size 2. [50, 4]
has product 200, having 2 zeros at the end,
[4, 20] — product 80, having 1 zero at the
end, [50, 20] — product 1000, having 3 zeros
at the end. Therefore, the maximum zeros at
the end of the product is 3.

Input : arr = {15, 16, 3, 25, 9}
        k = 3
Output : 3
Here, the subset [15, 16, 25] has product 6000.

Input : arr = {9, 77, 13}
        k = 3
Output : 0
Here, the subset [9, 77, 13] has product 9009
having no zeros at the end.
'''
MAX5 = 100


# Function to calculate maximum zeros.
def maximumZeros(arr, n, k):
    global MAX5

    # Initializing each value with -1 
    subset = [[-1] * (MAX5 + 5) for _ in range(k + 1)]

    subset[0][0] = 0

    for p in arr:

        pw2, pw5 = 0, 0

        # Calculating maximal power  
        # of 2 for arr[p]. 
        while not p % 2:
            pw2 += 1
            p //= 2

        # Calculating maximal power  
        # of 5 for arr[p]. 
        while not p % 5:
            pw5 += 1
            p //= 5

            # Calculating subset[i][j] for maximum
            # amount of twos we can collect by
        # checking first i numbers and taking
        # j of them with total power of five.
        for i in range(k - 1, -1, -1):

            for j in range(MAX5):

                # If subset[i][j] is not calculated.
                if subset[i][j] != -1:
                    subset[i + 1][j + pw5] = (
                        max(subset[i + 1][j + pw5],
                            (subset[i][j] + pw2)))

                    # Calculating maximal number of zeros.
    # by taking minimum of 5 or 2 and then
    # taking maximum.
    ans = 0
    for i in range(MAX5):
        ans = max(ans, min(i, subset[k][i]))

    return ans


# Driver function
arr = [50, 4, 20]
k = 2
n = len(arr)

print(maximumZeros(arr, n, k))

# This code is contributed by Ansu Kumari.

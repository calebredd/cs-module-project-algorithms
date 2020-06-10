'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    j = len(arr)-1
    for i in range(len(arr)-1):
        while arr[i] == 0 and j > i:
            arr[i], arr[j] = arr[j], arr[i]
            j-=1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

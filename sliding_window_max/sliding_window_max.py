'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from collections import deque 
def sliding_window_max(nums, k):
    # Your code here
    # arr = []
    # max=nums[0]
    # iMax = 0
    # for i in range(len(nums)-k+1):
        # if i>iMax:
            # max=nums[i]
        # j = i+1
        # if j<iMax:
            # j=iMax+1
        # while j < k+i:
            # if nums[j] > max:
                # max = nums[j]
                # iMax = j
            # j+=1
        # arr.append(max)

    arr = []
    for i in range(len(nums)-k+1 ):
        max = nums[i]
        for j in range(i, i+k):
        # try using after importing from collection, deque in place of the if.
            if nums[j]>max:
                max = nums[j]
            j+=1
        arr.append(max)
    return arr
    # arr=[]
    # que = deque()
    # max=nums[0]
    # for i in range(len(nums)-k+1):
        # que.append(nums[i])
        # if i > k:
            # que.popleft()
            # for j in que:
                # if j > max:
                    # max = j
            # arr.append(max)
        # elif i == k:
            # arr.append(max)
    # return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

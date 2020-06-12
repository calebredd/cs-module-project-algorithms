'''
Input: an integer
Returns: an integer
'''
cache={}
cache[2]=2
cache[1]=1
cache[0]=1
def eating_cookies(n):
    # Your code here
    if n in cache:
        return cache[n]
    else:
        cache[n-3]=eating_cookies(n-3)
        cache[n-2]=eating_cookies(n-2)
        cache[n-1]=eating_cookies(n-1)
        return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1) 

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")

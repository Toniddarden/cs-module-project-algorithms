'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
import collections
import time

def single_number(arr):
    # Your code here
    start = time.time()
    arr = [item for item, count in collections.Counter(arr).items() if count > 1]
    end = time.time()
    
    print(f"runtime for arr took {(end - start)} seconds") #2.288818359375e-05 seconds
    return arr

    print(arr)
    
    
    


    # pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
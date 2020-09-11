'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # selection sort 
    # for i in range(len(arr) -1):
    #     min_index = i       
    #     for j in range(i+1, len(arr) -1):
    #         if arr[min_index] > arr[j]:
    #             arr[min_index], arr[j] = arr[j], arr[min_index]
    # return arr # resulted in opposite output 
    
    temp = []
    # for every index in the array
    for i in arr:
        # if that index is 0
        if i == 0:
            # add it to the temp array 
            temp.append(i)
            continue
        # insert that index at position 0 in the temp array 
        temp.insert(0, i)
    return temp
        
                
        

    # pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
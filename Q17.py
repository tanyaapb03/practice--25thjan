#Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

#For example, given [100, 4, 200, 1, 3, 2], 
# the longest consecutive elements sequence should be [1, 2, 3, 4]. Its length is 4.

#psuedocode 
#Using hash set running in sequence identifyying value up and value down den if exist removing it from hash set 

def longestcon(nums):
    numbers= set()
    
    for num in nums:
        numbers.add(num)
        
        result =0
       
    for num in nums:
        
        count=1
        down=num-1
        while down in numbers:
            print(down)
            numbers.remove(down)
            down=down-1
            count=count+1
            print(count)

        up= num +1
        while up in numbers:
            print (up)
            numbers.remove(up)
            up=up+1
            count=count+1
            print(count)
        print(numbers)
        result=max(result,count)
    

    return result

print(longestcon([100, 4, 200, 1, 3, 2,5]))        









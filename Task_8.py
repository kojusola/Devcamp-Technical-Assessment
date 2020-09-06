# function to check the digits with threes in a range.
def num_with_three(n):
    # empty dictionary
    # count initailly equal to zero
    # numbers is initailly made an empty list.
    result={}
    count=0
    numbers=[]
    # interating the range between 0 and n(inclusive)
    for i in range(0,n+1):
        # a while loop that only breaks when the integer is less than 0
        while (i>0):
            # if the digit divided by 3 is equal to 1 or the digit divided by 10 is equalto three 
            # add to the count and the list
            if (i/3==1) or (i % 10 == 3):
                count+=1
                numbers.append(i)
            # the didvide the digit by 10 to go through the while loop again.
            i=i/10      
    result['count']=count
    result['numbers']=numbers
    print(result)
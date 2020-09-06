def prime_list(x):
    # function that accepts an array of integers and removes a list of prime numbers from them.
    # starting with an empty prime list
    primefromlist=[]
    # for each number in the array provided
    for number in x:
        # if the number is 2 then its added to the prime list
        if number==2:
            primefromlist.append(number)
        # if the number is not 2, then the condition below is carried out.
        # if the number is divisible by any number between 2 and that number, the for loop breaks
        # if not it is added to the prime list
        else:
            for z in range(2,number):
                if number%z==0:
                    break
            else:
                primefromlist.append(number)
    return primefromlist
                
x=[1,2,3,4,5,6,7,8,9]    
prime_list(x)
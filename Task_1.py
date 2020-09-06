#function to add even numbers and odd numbers
def sumnum(a):
    # setting the sum of numbers initially to zero
    sum_odd=0
    sum_even=0
    # each number in the array passes through this for loop
    for number in a:
        # if the number is even it is added to sum_even
        if number%2==0:
            sum_even+=number
        # if the number is odd it would be added to the sum_odd
        else:
            sum_odd+=number
    # print statement for sum_even and sum_odd
    print("Sum of even number:{}".format(sum_even))
    print("Sum of odd number:{}".format(sum_odd))
a=[1,2,3,4,5,6,7,8,9]
sumnum(a)
# import the math module
import math
# function to calculate standard deviation from an array of integers
def standarddeviations(y):
    # initially sum_num is set to 0
    sum_num=0
    #for each integer in the array, add to the sum_num
    for number in y:
        sum_num+=number
    # mean of the array is sum_num divided by the number of integers in the array
    mean =sum_num/len(y)
    # square of the difference is first set to 0
    # the square of difference between each integer and the mean is then added to the Square_of_difference
    square_of_difference=0
    for number in y:
        square_of_difference+= ((number-mean)**2)
    # variance is square_of_difference divided by number of integers minus 1
    variance=square_of_difference/(len(y)-1)
    #standard deviation is square root of variance
    return math.sqrt(variance)
y=[5,4,6,7]
standarddeviations(y)        
# function that takes in a string and gives letter with the hieghest frequency

def max_freq():
    # input the string
    string= input("Enter string:")
    # creating an empty dictionary with letter has key and frequecy as value
    freq_of_string={}
    # loop that takes every letter in the string, counts it and put in the dictionary
    for i in string:
        if i in freq_of_string:
            freq_of_string[i]+=1
        else:
            freq_of_string[i]=1
    # result gets the key with the maximum frequency(value)
    result = max(freq_of_string,key=freq_of_string.get)
    return result
max_freq()
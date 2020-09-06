# function that accepts integers and check if its a prime number
def check_prime(x):
    # if integer is one, it should return false since one is not a prime number.
    if x==1:
        return False
    # if integer is two, it should return True since two is a prime number.
    elif x==2:
        return True
    # if integer can be divided by any number between two and such integer 
    # it should return False since it is not a prime number
    # else return True
    else:
        for number in range(2,x):
            if x%number == 0:
                return False
            else:
                return True
check_prime(20)
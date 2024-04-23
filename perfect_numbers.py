def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
        
    num = number
    count = 1
    sum = 0
    while count<num:
        if num%count == 0:
            sum = sum + count
        count+=1
    if sum == num:
        return ("perfect")
    if num < sum:
        return("abundant")
    if num > sum:
        return("deficient")
     

print(classify(2))
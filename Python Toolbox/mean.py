def mean(*x): 
    """Returns the mean of all the numbers"""
    total_sum = 0 # Initial sum
    n = len(x) # Number of arguments
    for i in x:
        total_sum = total_sum + i
    return total_sum/n
print((mean(4,5), mean(30,35,40)))


output: (4.5, 35.00)

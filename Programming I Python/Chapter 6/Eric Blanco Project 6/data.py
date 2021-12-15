#this is the data module, which holds functions for max, min, avg, midrange, and
#validation

#function for data validation
def validScore(l, u, value):
    if value >= l and value <= u:
        return True
    else:
        return False

#function for finding the max value
def updateMax(max, value):
    if value > max:
        max = value

    return max

#function for finding the min value
def updateMin(min, value):
    if value < min:
        min = value

    return min

#function for finding the average
def mean(total, count):
    return total / count



#function for finding the midrange
def midRange(max, min):
    return (max + min) / 2





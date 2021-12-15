#this program validates the data read to match the bounds set by the user

#the following will be entered before function is called:
#lower = int(input('Enter the lowest possible limit: '))
#upper = int(input('Enter the highest possible limit: '))
#It is going to read in values for 'value'

def validateData(low, high, value):
    if value >= low and value <= high:
        included = True
    else:
        included = False

    return included
    

    
    
    

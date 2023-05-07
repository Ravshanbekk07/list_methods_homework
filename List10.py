def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    i = 0
    numbs_of_o = 0
    numbs_of_1 = 0
    while i < len(list1):
        if not list1[i]%2:
            numbs_of_1+=1
        else:
            numbs_of_o+=1
        i+=1
    
    return numbs_of_1,numbs_of_o


v = main([1, 0, 0, 0, 1, 0, 1, 0])
print(v)
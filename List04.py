def main(numbers,i):
    """
    You are given a list of numbers. i Delete and return the number in the index.
    Args:
        numbers(list): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    numbers.remove(i)

    return numbers[3]

v = main([4,7,3,2,8],4)
print(v)
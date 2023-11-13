def myzip(it1, it2):
    
    # Custom implementation of the zip function.
    # Takes two iterables and returns a list of tuples,
    # where each tuple contains elements from the iterables
    # paired together.
    
    min_length = min(len(it1), len(it2))  # To handle iterables of different lengths
    return [(it1[i], it2[i]) for i in range(min_length)]

# Example Usage
if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    zipped = myzip(list1, list2)
    print(zipped)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

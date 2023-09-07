def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    
    # sum_pair=[]
    # count=0
    # while count != goal:
    #     for num in nums:
    #         sum_pair.append(num)
    #         count += num
        
    # return sum_pair
    
        
    already_visited = set()

    for i in nums:
        difference = goal - i

        if difference in already_visited:
            return (difference, i)

        already_visited.add(i)

    return ()
        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        """we initalize already_visited to an epty set.  this will be used to keep track of nums that have been encourntered
        1. begin loop.  i=4.  2=6-4
        2. 2 is not in set so we add
          already_visited=(4)
        3. i=2      4=6-2  4 is in already visited so return difference of current loop which is 4 and current i which is 2
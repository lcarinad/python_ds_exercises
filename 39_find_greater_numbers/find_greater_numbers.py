def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    length=len(nums)
    counter =0
    indie=0
    index_of_num=nums.index(indie)
    for num in nums:
        length=length-1
        while length>0:
            if num >num[index_of_num]:
                count+=1
            
            indie+=1
            
    return counter
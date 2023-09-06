def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # list_from_phr=list(phrase)
    # letter_count={}
    # counter=0

    # for char in list_from_phr:
    #     if char not in letter_count: 
    #         letter_count[char]=1
    #     else:
    #         letter_count[char]+=1
    # return letter_count
    
    
    counter={}
    for char in phrase:
        counter[char]=counter.get(char, 0)+1
    return counter
          

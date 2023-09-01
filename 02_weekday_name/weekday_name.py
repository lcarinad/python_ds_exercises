def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    weekday_name=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',  'Friday', 'Saturday']
# solution with if else statement
    # if day_of_week == 0:
    #     return None
    # elif day_of_week <=7:
    #     return weekday_name[day_of_week-1]
    # else:
    #     return None

# solution with ternary using range
    return weekday_name[day_of_week-1] if (day_of_week in range(1,8)) else None
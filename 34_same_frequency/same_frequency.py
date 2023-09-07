def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1=str(num1)
    num2=str(num2)
    num1_counts={digit:num1.count(digit) for digit in num1}
    num2_counts={digit:num2.count(digit) for digit in num2}
    return num1_counts==num2_counts
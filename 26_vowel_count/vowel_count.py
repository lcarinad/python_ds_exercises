def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    # vowel_count={}
    vowels={"a","e", "i", "o","u"}
    for vowel in vowels:
        for char in phrase.lower():
            if vowel == char:
                if vowel in vowel_count:
                    vowel_count[vowel]=phrase.lower().count(char)
                else: 
                    vowel_count[vowel]=1
    
    return vowel_count

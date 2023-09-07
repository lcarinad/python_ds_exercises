def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase_list=phrase.split(" ")
    capitalize_words=[word.capitalize() for word in phrase_list]
    titelized_phrase=" ".join(capitalize_words)
    return titelized_phrase
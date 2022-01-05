def is_even(number):
    ''' Returns True if **number** is even or False if it is odd. '''
    surplus = not(number % 2)
    return bool(surplus)

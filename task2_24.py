def is_palindrom (any_string):
    if any_string.lower() == any_string[::-1].lower():
        return print ('True')
    else: 
        return print ('False')


string_ = input('Type any string: ') 

is_palindrom(string_)
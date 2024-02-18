# BEGIN (write your solution here)
def get_number_explanation(number:int)-> str:
    match number:
        case 0:
            return 'just a number'
        case 666:
            return 'devil number'
        case 42:
            return'answer for everything'
        case 7:
            return 'prime number'
# END




get_number_explanation(8)  # just a number
get_number_explanation(666)  # devil number
get_number_explanation(42)  # answer for everything
get_number_explanation(7)  # prime number



def is_palindrome(word: str) -> bool:

    tmp: str = None
    tmp = word[::-1]
    print(f"word: [{word} and {tmp} {tmp == word}")
    if tmp == word:
        return True
    else:
        return False


is_palindrome('motor')
is_palindrome('bulb')
is_palindrome('blablab')
is_palindrome('rotor')
is_palindrome('abba')
is_palindrome('r')
is_palindrome('')

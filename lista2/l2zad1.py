import string
import random

def password_generator(length = 8, signs = string.ascii_letters + string.digits + string.punctuation):
    """
    Generate a random password of given length and with given signs

    ...

    Input
    ----------
    length (int): The lenghth of the password (default 8)
    signs (str): A string of characters that can be used in the password. Default includes all uppercase and lowercase letters, digits, and punctuation symbols.

    Raises
    ----------
    TypeError: If variable "signs" type is not string
    TypeError: If "length" type is not integer

    Output
    ----------
    The password of given length and with given signs
    """
    
    if type(signs) != str:
        raise TypeError("Sings type has to be string")
    if type(length) != int or length < 1:
        raise TypeError("Length type has to be integer > 0")
    return "".join([random.choice(signs) for _ in range(length)])

if __name__ == "__main__":
    print(password_generator(150,"123"))

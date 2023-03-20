import string
import random

def password_generator(length = 8, signs = string.ascii_letters + string.digits + string.punctuation):
    """ INSERT DOCSTRING """
    if type(signs) != str:
        raise TypeError("Sings type have to be string")
    return "".join([random.choice(signs) for i in range(length)])

print(password_generator(150,123))
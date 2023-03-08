import random
import math
import numpy as np

class Vector:
    """
    This module provides a Vector class that can be used to represent vectors in n-dimensional space

    ...

    Attributes
    ----------
    vector (numpy.ndarray): A numpy array representing the vector
    dim (int): An integer representing the dimension of the vector

    Methods
    ----------
    set_random_el(self): Fills the vector with random elements
    __str__(self): Returns the string representation of the vector
    insert_el(self, el_list): Inserts a list/tuple of elements into the vector
    __add__(self, v2): Adds two vectors
    __sub__(self, v2): Subtracts two vectors
    __mul__(self, v2): Returns the scalar product of the two vectors
    scalar_mul(self, scalar): Multiplies the vector by a scalar
    get_length(self): Computes the length of the vector
    get_sum(self): Computes the sum of all the vectors' elements
    __getitem__(self, index): Gets an element from the vector given an index
    __contains__(self, el): Checks if an element is in the vector
    """
    
    def __init__(self, dim=3):
        """
        Initializes a new instance of the Vector class

        ...

        Parameters
        ----------
        vector (numpy.ndarray): A numpy array representing the vector
        dim (int): An integer representing the dimension of the vector
        """
        self.vector = np.zeros(dim)
        self.dim = dim

    def set_random_el(self):
        """
        Fills the vector with random elements

        ...

        Output
        ----------
        vector (numpy.ndarray): A numpy array representing the vector with float numbers from -100 to 100
        """
        for i in range(self.dim):
            self.vector[i] = random.uniform(-100,100)
        return self.vector

    def __str__(self):
        """
        Returns the string representation of the vector

        ...

        Output
        ----------
        str(vector_list) (str): A string representing the vector
        """
        vector_list = []
        for i in range(self.dim):
            vector_list.append(self.vector[i])
        return str(vector_list)
    
    def insert_el(self, el_list):
        """
        Inserts a list/tuple of elements into the vector

        ...

        Input
        ----------
        el_list (list/tuple): A list/tuple of elements to be inserted into the vector

        Raises
        ----------
        TypeError: If given argument is not a list or tuple
        ValueError: If number of elements in a given argument is not equal to the dimension of the vector

        Output
        ----------
        vector (Vector): A Vector object representing the vector with the inserted elements
        """
        if type(el_list) != list and type(el_list) != tuple:
            raise TypeError("Given argument has to be a list or tuple")
        elif self.dim != len(el_list):
            raise ValueError("Number of given arguments is not equal to the dimension of the vector")
        else:
            for i in range(self.dim):
                self.vector[i] = el_list[i]
        return self.vector
    
    def __add__(self, v2):
        """
        Adds two vectors

        ...

        Input
        ----------
        v2 (Vector): A Vector object representing the second vector to be added

        Raises
        ----------
        ValueError: If the two vectors have different dimensions

        Output
        ----------
        self.vector (Vector): A Vector object representing the sum of the two vectors
        """
        if self.dim != v2.dim:
            raise ValueError("Vectors have different dimensions")
        else:
            for i in range(self.dim):
                self.vector[i] += v2.vector[i]
        return self.vector

    def __sub__(self, v2):
        """
        Subtracts two vectors

        ...

        Input
        ----------
        v2 (Vector): A Vector object representing the second vector to be subtracted

        Raises
        ----------
        ValueError: If the two vectors have different dimensions

        Output
        ----------
        self.vector (Vector): A Vector object representing the subtraction of the two vectors
        """
        if self.dim != v2.dim:
            raise ValueError("Vectors have different dimensions")
        else:
            for i in range(self.dim):
                self.vector[i] -= v2.vector[i]
        return self.vector

    def __mul__(self, v2):
        """
        Returns the scalar product of the two vectors

        ...

        Input
        ----------
        v2 (Vector): A Vector object representing the second vector to be used to compute the scalar product

        Raises
        ----------
        ValueError: If the two vectors have different dimensions

        Output
        ----------
        v3 (numpy.float64): Scalar product of the two vectors
        """
        if self.dim != v2.dim:
            raise ValueError("Vectors have different dimensions")
        else:
            v3 = 0
            for i in range(self.dim):
                v3 += self.vector[i] * v2.vector[i]
        return v3

    def scalar_mul(self, scalar):
        """
        Multiplies the vector by a scalar

        ...

        Input
        ----------
        scalar (int/float): A scalar to be used to perform a multiplication

        Raises
        ----------
        ValueError: If scalar type is not int or float

        Output
        ----------
        self.vector (Vector): A Vector object representing the multiplication of the vector and scalar
        """
        if type(scalar) != int and type(scalar) != float:
            raise ValueError("Wrong scalar data type")
        else:
            for i in range(self.dim):
                self.vector[i] *= scalar
        return self.vector

    def get_length(self):
        """
        Computes the length of the vector

        ...

        Output
        ----------
        math.sqrt(length) (float): Length of the vector
        """
        length = 0
        for i in range(self.dim):
            length += (self.vector[i])**2
        return math.sqrt(length)

    def get_sum(self):
        """
        Computes the sum of all the vectors' elements

        ...

        Output
        ----------
        sum(vector) (float): The sum of all the vectors' elements
        """
        return sum(self.vector)

    def __getitem__(self, index):
        """
        Gets an element from the vector given an index

        ...

        Input
        ----------
        index (int): Index number of the vetcors' element

        Raises
        ----------
        TypeError: If index type is not int
        IndexError: If index is out of range

        Output
        ----------
        vector[index] (numpy.float64): Element from the vector based on the index number
        """
        if type(index) != int:
            raise TypeError("Index type has to be an integer")
        elif index < 0 or index >= self.dim:
            raise IndexError("Index out of range")
        return self.vector[index]

    def __contains__(self, el):
        """
        Checks if an element is in the vector

        ...

        Output
        ----------
        True: If an element is in the vector
        False: If an element is not in the vector
        """
        if el in self.vector:
            return True
        else:
            return False
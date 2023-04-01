import re

def column_add(operation:str):
    """
    Return formatted column of addition or subtraction

    ...

    Input
    ----------
    operation (str): The mathematical operation to perform

    Raises
    ----------
    TypeError: If given the given argument is not of type string

    Output
    ----------
    column (str): The formatted column of the mathematical operation
    """

    if type(operation) != str:
        raise TypeError("Given argument has to be of type string")
    
    result = eval(operation)
    
    op_list = re.findall(r'[+-]?\d+', operation)
    op_list = [expression.lstrip("+") for expression in op_list]

    len_list = []
    for i in range(len(op_list)):
        len_list.append(len(op_list[i]))
    len_list.append(len(str(result)))
    
    max_length = max(len_list) + 3

    str_op_list = []
    for i in range(len(op_list)-1):
        str_op_list.append(op_list[i].rjust(max_length))
    
    str_op_list.append("+" + op_list[-1].rjust(max_length-1))
    str_result = str(result).rjust(max_length)
    line = "-"*max_length

    column = ""
    for i in range(len(str_op_list)):
        column += str_op_list[i] + "\n"
    column += line + "\n" + str_result

    return column


def column_multiply(operation:str):
    """
    Return formatted column of multiplication

    ...

    Input
    ----------
    operation (str): The mathematical operation to perform

    Raises
    ----------
    TypeError: If given the given argument is not of type string or numbers to multiply are not integers
    NotImplementedError: If multiplication on more than 2 numbers is performed

    Output
    ----------
    column (str): The formatted column of the mathematical operation
    """
    
    if type(operation) != str:
        raise TypeError("Given argument has to be of type string")
 
    result = eval(operation)
    op_list = operation.split("*")

    if len(op_list) > 2:
        raise NotImplementedError("Function can multiply only 2 integers")
    
    try:
        int(op_list[0])
        int(op_list[1])
    except:
        raise TypeError("Function can multiply only integers")

    add_list = []
    complete_add_list = []
    for i in range(len(op_list[1])-1, -1, -1):
        carry = 0
        for j in range(len(op_list[0])-1, -1, -1):
            prod = int(op_list[1][i]) * int(op_list[0][j]) + carry
            carry = prod//10
            prod %= 10
            add_list.append(prod)
        if carry != 0:
            add_list.append(carry)
        complete_add_list.append("".join(map(str, add_list[::-1])))
        add_list = []

    len_list = []
    for i in range(len(op_list)):
        len_list.append(len(op_list[i]))
    len_list.append(len(str(result)))

    for i in range(len(complete_add_list)):
        len_list.append(len(complete_add_list[i]))
    
    max_length = max(len_list) + len(complete_add_list) + 1

    multi_op_list = []
    for i in range(len(op_list)-1):
        multi_op_list.append(op_list[i].rjust(max_length))
    
    multi_op_list.append("*" + op_list[-1].rjust(max_length-1))
    str_result = str(result).rjust(max_length)
    line = "-"*max_length

    add_op_list = []
    for i in range(len(complete_add_list)-1):
        add_op_list.append(complete_add_list[i].rjust(max_length-i))

    add_op_list.append("+" + complete_add_list[-1].rjust(max_length-len(complete_add_list)))

    column = ""
    for i in range(len(multi_op_list)):
        column += multi_op_list[i] + "\n"
    column += line + "\n"
    for i in range(len(add_op_list)):
        column += add_op_list[i] + "\n"
    column += line + "\n" + str_result

    return column

if __name__ == "__main__":
    print(column_add("5+5-300+5-300-800-5+8"))
    print("/////////////////////////")
    print(column_multiply("1345*342"))

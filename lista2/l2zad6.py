import re

def column_add(operation:str):
    """INSERT DOCSTRING"""
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
    result = eval(operation)
    op_list = operation.split("*")

    """
    add_list = []
    for i in range(len(op_list[1])-1, -1, -1):
        carry = 0
        for j in range(len(op_list[0])-1, -1, -1):
            prod = int(op_list[1][i]) * int(op_list[0][j]) + carry
            carry = prod//10
            prod %= 10
            add_list.append(prod)
    add_list.append(carry)
    """  

    len_list = []
    for i in range(len(op_list)):
        len_list.append(len(op_list[i]))
    len_list.append(len(str(result)))
    
    max_length = max(len_list) + 3

    str_op_list = []
    for i in range(len(op_list)-1):
        str_op_list.append(op_list[i].rjust(max_length))
    
    str_op_list.append("*" + op_list[-1].rjust(max_length-1))
    str_result = str(result).rjust(max_length)
    line = "-"*max_length

    column = ""
    for i in range(len(str_op_list)):
        column += str_op_list[i] + "\n"
    column += line + "\n" + str_result

    return column

if __name__ == "__main__":
    print(column_add("5+5-300+5-300-800-5+8"))

    print(column_multiply("235*72"))


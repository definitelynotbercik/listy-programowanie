def paranthesis_check(equation):
    """INSERT DOCSTRING"""

    par_list = []
    for char in equation:
        if char in ["(",")","[","]","{","}","<",">"]:
            par_list.append(char)
    if len(par_list)%2 != 0:
        return False

    for i, par  in enumerate(par_list):
        if i+1 > len(par_list)/2:
            break
        elif par_list[i] == par_list[i+1]:
            return False
        elif par == "(":
            if par_list[-i-1] != ")":
                return False
        elif par == "[":
            if par_list[-i-1] != "]":
                return False
        elif par == "{":
            if par_list[-i-1] != "}":
                return False
        elif par == "<":
            if par_list[-i-1] != ">":
                return False

    return True


if __name__ == "__main__":
    print(paranthesis_check("2[(3+5)-8]"))
    
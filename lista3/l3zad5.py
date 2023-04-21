def bracket_check(equation):
    """INSERT DOCSTRING"""

    bracket_list = []
    for char in equation:
        if char in ["(",")","[","]","{","}","<",">"]:
            bracket_list.append(char)
    if len(bracket_list)%2 != 0:
        return False

    for i, par  in enumerate(bracket_list):
        if i+1 > len(bracket_list)/2:
            break
        elif bracket_list[i] == bracket_list[i+1]:
            return False
        elif par == "(":
            if bracket_list[-i-1] != ")":
                return False
        elif par == "[":
            if bracket_list[-i-1] != "]":
                return False
        elif par == "{":
            if bracket_list[-i-1] != "}":
                return False
        elif par == "<":
            if bracket_list[-i-1] != ">":
                return False

    return True


if __name__ == "__main__":
    print(bracket_check("3*[*2(3+5)]"))
    
import re

def is_int_convertible(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def sum_muls(string):
    pattern=r"mul\((.*?)\)"
    matches = re.findall(pattern, string)
    sum_ = 0
    for match in matches:
        
        operands = match.split(",")
        if len(operands) == 2:
            left_operand = operands[0].strip()
            right_operand = operands[1].strip()
            if is_int_convertible(left_operand) and is_int_convertible(right_operand):
                sum_ += int(left_operand) * int(right_operand)
                
        recursive_mul_sum = sum_muls(match + ")") # The + ")" deals with edge cases such as mul(mul(3,2) where the match is "mul(3,2"
        sum_ += recursive_mul_sum
                
    return sum_
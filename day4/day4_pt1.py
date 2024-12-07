
def get_horizontal_lines(string):
    return string.split("\n")

def get_vertical_lines(string):
    
    vertical_lines = []
    
    horizontal_lines = get_horizontal_lines(string)
    width = len(horizontal_lines[0])
    height = len(horizontal_lines)
    
    for i in range(0,width):
        vertical_line = ""
        for j in range(0,height):
            vertical_line += horizontal_lines[j][i]
            
        vertical_lines.append(vertical_line)
        
    return vertical_lines

def get_diagonal_up_lines(string):

    horizontal_lines = get_horizontal_lines(string)
    width = len(horizontal_lines[0])
    height = len(horizontal_lines)
    diagonal_lines = []

    # top diagonals    
    for i in range(0,width):
        
        diagonal_line = ""
        x = 0
        y = i

        while y >= 0:
            diagonal_line += horizontal_lines[y][x]
            x += 1
            y -= 1

        diagonal_lines.append(diagonal_line)
        
    # bottom diagonals    
    for i in range(1,width):
        
        diagonal_line = ""
        x = i
        y = height-1

        while x < width:
            diagonal_line += horizontal_lines[y][x]
            x += 1
            y -= 1

        diagonal_lines.append(diagonal_line)

    return diagonal_lines

def get_diagonal_down_lines(string):

    horizontal_lines = get_horizontal_lines(string)
    width = len(horizontal_lines[0])
    height = len(horizontal_lines)
    diagonal_lines = []

    # top diagonals    
    for i in range(0,width):
        
        diagonal_line = ""
        x = i
        y = 0

        while x < width:

            diagonal_line += horizontal_lines[y][x]
            x += 1
            y += 1

        diagonal_lines.append(diagonal_line)
        
    # bottom diagonals    
    for i in range(0,width-1):
        
        diagonal_line = ""
        x = i
        y = height-1

        while x >= 0:

            diagonal_line += horizontal_lines[y][x]
            x -= 1
            y -= 1

        diagonal_lines.append(diagonal_line)

    return diagonal_lines

data = open("input.txt").read()
# data = open("mini_input.txt").read()


lines = get_horizontal_lines(data) + get_vertical_lines(data) + get_diagonal_down_lines(data) + get_diagonal_up_lines(data)

sum_ = 0
for line in lines:
    sum_ += line.count("XMAS") + line[::-1].count("XMAS")
    
    
# for line in get_diagonal_down_lines(data):
#     print(line)
#     print(line.count("XMAS") + line[::-1].count("XMAS"))
    
print(sum_)
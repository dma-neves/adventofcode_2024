
def get_horizontal_lines(string):
    return string.split("\n")

data = open("input.txt").read()
#data = open("mini_input_pt2.txt").read()


lines = get_horizontal_lines(data)

sum_ = 0

height = len(lines)
width = len(lines[0])
    
for y in range(1,height-1):

    for x in range(1,width-1):

        if lines[y][x] == 'A':

            # M
            #  A
            #   S
            mas_0 = lines[y-1][x-1] == 'M' and lines[y+1][x+1] == 'S'
    
            # S
            #  A
            #   M
            mas_1 = lines[y-1][x-1] == 'S' and lines[y+1][x+1] == 'M'

            #   M
            #  A
            # S
            mas_2 = lines[y-1][x+1] == 'M' and lines[y+1][x-1] == 'S'

            #   S
            #  A
            # M
            mas_3 = lines[y-1][x+1] == 'S' and lines[y+1][x-1] == 'M'

            if (mas_0 or mas_1) and (mas_2 or mas_3):
                sum_ += 1

# for line in get_diagonal_down_lines(data):
#     print(line)
#     print(line.count("XMAS") + line[::-1].count("XMAS"))
    
print(sum_)
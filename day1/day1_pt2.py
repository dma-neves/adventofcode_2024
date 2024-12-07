def read_values_from_file(filename):
    left_values = []
    right_values = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            left_value = int(parts[0])
            right_value = int(parts[1])
            left_values.append(left_value)
            right_values.append(right_value)
            
            
        return (left_values, right_values)


filename = "input.txt"  # Replace with your actual filename
(left_values, right_values) = read_values_from_file(filename)


right_values_map = {}

for value in right_values:
    
    if value in right_values_map:
        right_values_map[value] += 1
    else:
        right_values_map[value] = 1
        

sum_ = 0
for value in left_values:
    
    if value in right_values_map:
        sum_ += value * right_values_map[value]
    
print(sum_)
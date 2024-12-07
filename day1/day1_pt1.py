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

left_values.sort()
right_values.sort()

sum_ = 0
for i in range(0, len(left_values)):
    sum_ += abs(left_values[i] - right_values[i])
    
print(sum_)
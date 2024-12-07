def read_values_from_file(filename):
    reports = []
    with open(filename, 'r') as file:
        for line in file:
            levels_txt = line.strip().split()
            levels = [int(level_txt) for level_txt in levels_txt]
            reports.append(levels)
            
            
        return reports


filename = "input.txt"  # Replace with your actual filename
reports = read_values_from_file(filename)


num_safe = 0
for report in reports:
    
    if len(report) <= 1:
        num_safe += 1
    else:
        
        ascending = report[1] > report[0]
                    
        safe = all(
            1 <= abs(report[i] - report[i - 1]) <= 3 and
            (report[i] > report[i-1] ) == ascending
            for i in range(1, len(report))
        )
        
        if safe:
            num_safe += 1
            
print(num_safe)
            
            
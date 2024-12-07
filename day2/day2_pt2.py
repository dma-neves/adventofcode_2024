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
        
        remove_index = 0
        while (not safe) and remove_index < len(report):
            
            
            sub_report = report[:remove_index] + report[remove_index+1:]
            ascending = sub_report[1] > sub_report[0]

            safe = all(
                1 <= abs(sub_report[i] - sub_report[i - 1]) <= 3 and
                (sub_report[i] > sub_report[i-1] ) == ascending
                for i in range(1, len(sub_report))
            )
            
            remove_index += 1
        
        if safe:
            num_safe += 1
            
print(num_safe)
            
            
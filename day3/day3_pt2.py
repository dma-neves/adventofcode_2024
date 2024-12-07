import re

from sum_muls import sum_muls

def get_active_sections(string):
    
    active_sections = []
    
    string_to_evaluate = string
    
    while string_to_evaluate != "":
        disabled_section_start = string_to_evaluate.find("don't()")
        
        if disabled_section_start == -1:
            active_sections.append(string_to_evaluate)
            string_to_evaluate = ""
        else:
            active_sections.append(string_to_evaluate[:disabled_section_start])
                    
            string_to_evaluate = string_to_evaluate[disabled_section_start:]
            disabled_section_end = string_to_evaluate.find("do()")
            string_to_evaluate = string_to_evaluate[disabled_section_end:]
        
    
    
    
    return active_sections

data = open("input.txt").read().strip()


active_sections = get_active_sections(data)

sum_ = 0
for active_section in active_sections:
    # print("ACTIVE SEC: ", active_section)
    sum_ += sum_muls(active_section)
    

print(sum_)


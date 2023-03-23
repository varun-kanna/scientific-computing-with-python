def arithmetic_arranger(problems, solution=False):
  # Checking if amount of problems is possible in the first place
  if len(problems) > 5:
    return "Error: Too many problems."
    
  first_line = ""
  second_line = ""
  third_line = ""
  fourth_line = ""  
  
  for i in problems:
    element = i.split()
    fnum = element[0]
    operator = element[1]
    snum = element[2]
    
    # Outlier test cases
    if len(fnum) > 4 or len(snum) > 4:
      return "Error: Numbers cannot be more than four digits."
    if ((operator == "/") or (operator == "/")):
      return "Error: Operator must be '+' or '-'."
    if (fnum.isdigit() == False ) or (snum.isdigit() == False):
      return "Error: Numbers must only contain digits."
    
    # If the operator is valid (addition or subtraction)
    if (operator == "+") or (operator == "-"):
      
      sum = ""
      if operator == "-":
        sum = str(int(fnum) - int(snum))
      if operator == "+":
        sum = str(int(fnum) + int(snum))
    
      max_len = max(len(fnum),len(snum)) + 2
      
      
      if i != i[-1]:
        first_line += str(fnum).rjust(max_len) + "    "
        second_line += operator + str(snum).rjust(max_len-1) + "    "
        third_line += ((max_len)* "-") + "    "
        fourth_line += sum.rjust(max_len) + "    "
        
      else:  
        first_line += str(fnum).rjust(max_len) 
        second_line += operator + str(snum).rjust(max_len-1) 
        third_line += ((max_len)* "-")
        fourth_line += sum.rjust(max_len)
        
      
  if solution:
    return first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + third_line.rstrip() + "\n" + fourth_line.rstrip()
        
  else:
    return first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + third_line.rstrip()

  

  
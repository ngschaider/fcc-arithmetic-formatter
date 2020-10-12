import re

"""
parsed data structure
0 => first number
1 => operator
2 => second number
3 => answers (None if display_answers=False)
4 => length of the largest number
"""
def arithmetic_arranger(problems, display_answers=False):
  parsed = parse_data(problems)

  if type(parsed) != list:
    return parsed

  parsed = calculate_answers(parsed)
  parsed = calculate_lengths(parsed)

  output = ""
  spacer = " " * 4

  for i,problem in enumerate(parsed):
    if i:
      output += spacer;
    output += format_number(problem[0], problem[4] + 2)

  output += "\n"

  for i,problem in enumerate(parsed):
    if i:
      output += spacer
    output += problem[1] + " " + format_number(problem[2], problem[4])
    

  output += "\n"

  for i,problem in enumerate(parsed):
    if i:
      output += spacer
    output += "-" * (problem[4] + 2)

  if display_answers:
    output += "\n"
    for i,problem in enumerate(parsed):
      if i:
        output += spacer
      output += format_number(problem[3], problem[4] + 2)

  return output

def calculate_answers(parsed):
  for problem in parsed:
    if problem[1] == "+":
      problem.append(problem[0] + problem[2])
    if problem[1] == "-":
      problem.append(problem[0] - problem[2])

  return parsed

def calculate_lengths(parsed):
  for problem in parsed:
    problem.append(len(str(max(problem[0], problem[2], problem[3]))));

  return parsed

def format_number(number, length):
  if(len(str(number)) < 0):
    number = number - 1
  spaces = " " * (length - len(str(number)))
  return spaces + str(number)

def parse_data(problems):
  if len(problems) > 5:
    return "Error: Too many problems."

  ret = []
  for problem in problems:
    splits = re.split("\s", problem)

    if(splits[1] != "+" and splits[1] != "-"):
      return "Error: Operator must be '+' or '-'."

    if(len(splits[0]) > 4 or len(splits[2]) > 4):
      return "Error: Numbers cannot be more than four digits."

    try:
      el = [int(splits[0]), splits[1], int(splits[2])]
    except ValueError:
      return "Error: Numbers must only contain digits."
    
    
    ret.append(el)

  return ret 
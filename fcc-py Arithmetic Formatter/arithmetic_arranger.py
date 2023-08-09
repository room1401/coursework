import re

def arithmetic_arranger(problems, solve = False):

  def checkError(lst, msg=[]):
    if len(lst) > 5:
      return "Error: Too many problems."
    for obj in lst:
      if not (re.search('\s[+|-]\s', obj)):
        msg.append("Error: Operator must be '+' or '-'.")
      if not (re.search('^\d+\s.\s\d+$', obj)):
        msg.append("Error: Numbers must only contain digits.")
      if len(max(obj.split(), key=len)) > 4:
        msg.append("Error: Numbers cannot be more than four digits.")
    return msg

  if checkError(problems):
    return '\n'.join(checkError(problems))

  output = ['', '', '', ''] if solve else ['', '', '']
  for prob in problems:
    margin = len(max(prob.split(), key=len)) + 2
    padding = '' if prob == problems[-1] else ' ' * 4
    num1, optr, num2 = prob.split()
    output[0] += num1.rjust(margin) + padding
    output[1] += optr + num2.rjust(margin - 1) + padding
    output[2] += '-' * margin + padding
    if solve:
      output[3] += str(int(num1) + int(optr + num2)).rjust(margin) + padding
  
  return '\n'.join(output)

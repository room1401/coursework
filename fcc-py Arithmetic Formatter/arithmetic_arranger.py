import re

def arithmetic_arranger(problems, solve = False):

  def checkError(lst):
    msg = []
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

  ln1, ln2, ln3 = "", "\n", "\n"
  ln4 = "\n" if solve else ""
  for i in range(len(problems)):
    margin = len(max(problems[i].split(), key=len)) + 2
    padding = "" if i == len(problems) - 1 else " " * 4
    num1, optr, num2 = problems[i].split()
    ln1 += num1.rjust(margin) + padding
    ln2 += optr + num2.rjust(margin - 1) + padding
    ln3 += "-" * margin + padding
    if solve:
      ln4 += str(int(num1) + int(optr + num2)).rjust(margin) + padding
  
  return ln1 + ln2 + ln3 + ln4

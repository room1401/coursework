'''
The programs will consist of rows, and each row will be in one of the 
following formats:

- PRINT [value]: prints the value
- MOV [variable] [value]: assigns the value to the variable
- ADD [variable] [value]: adds the value to the variable
- SUB [variable] [value]: subtracts the value from the variable
- MUL [variable] [value]: multiplies the variable by the value
- [location]:: names a line of code, so it can be jumped to from elsewhere
- JUMP [location]: jumps to the location specified
- IF [condition] JUMP [location]: if the condition is true, jump to the 
  location specified
- END: finish execution

Please write a function named run(program), which takes a list containing 
the program commands as its argument. Each item on the list is a line of 
code in the program. The function should return a new list, which contains 
the results of the PRINT commands executed during the program's run.

You may assume the function will only be given programs which are entirely 
in the correct format. You do not have to implement any input validation 
or error handling.
'''

# Write your solution here
def conv(lst):
    for i, val in enumerate(lst):
        if val.isalpha():
            lst[i] = f"var['{val}']"

    return " ".join(lst)

def calc(id, op1, op2, var):
    op1 = eval(conv([op1]))
    op2 = eval(conv([op2]))
    op = {"MOV":(0,0,2), "MUL":(1,1,1), "ADD":(1,0,2), "SUB":(1,0,0)}
    i, j, k = op[id]
    return op1 * i  * [1, op2][j] + op2 * [-1, 0, 1][k]

def run(pgm):
    output = []
    var = dict((chr(x), 0) for x in range(65, 91))
    loca = dict()
    for i, cmd in enumerate(pgm):
        if cmd.endswith(":"):
            loca[cmd[:-1]] = i
    
    step = 0
    while step < len(pgm):
        cmd, *par = pgm[step].split()
        if cmd == "PRINT":
            output.append(eval(conv([par[0]])))
        elif cmd == "JUMP":
            step = loca[par[0]]
        elif len(par) == 2:
            var[par[0]] = calc(cmd, *par, var)
        elif cmd == "IF":
            if eval(conv(par[:3])):
                step = loca[par[-1]]
        elif cmd == "END":
            break
        
        step += 1

    return output

if __name__ == "__main__":
    test = [
      [
        "MOV A 1", "MOV B 2", "PRINT A", "PRINT B", "ADD A B", 
        "PRINT A", "END"
      ],
      [
        'MOV A 1', 'MOV B 10', 'begin:', 'IF A >= B JUMP quit', 'PRINT A', 
        'PRINT B', 'ADD A 1', 'SUB B 1', 'JUMP begin', 'quit:', 'END'
      ],
      [
        'MOV A 1', 'MOV B 1', 'begin:', 'PRINT A', 'ADD B 1', 
        'MUL A B', 'IF B <= 10 JUMP begin', 'END'
      ],
      [
        'MOV N 50', 'MOV A 3', 'begin:', 'MOV B 2', 'MOV Z 0', 'test:', 
        'MOV C B', 'new:', 'IF C == A JUMP error', 'IF C > A JUMP over', 
        'ADD C B', 'JUMP new', 'error:', 'MOV Z 1', 'JUMP over2', 'over:', 
        'ADD B 1', 'IF B < A JUMP test', 'over2:', 'IF Z == 1 JUMP over3', 
        'PRINT A', 'over3:', 'ADD A 1', 'IF A <= N JUMP begin'
      ],
      [
        'MOV N 100', 'PRINT 2', 'MOV A 3', 'start:', 'MOV B 2', 'MOV Z 0',
        'test:', 'MOV C B', 'new:', 'IF C == A JUMP virhe', 
        'IF C > A JUMP pass_by', 'ADD C B', 'JUMP new', 'virhe:', 'MOV Z 1', 
        'JUMP pass_by2', 'pass_by:', 'ADD B 1', 'IF B < A JUMP test', 
        'pass_by2:', 'IF Z == 1 JUMP pass_by3', 'PRINT A', 'pass_by3:', 
        'ADD A 1', 'IF A <= N JUMP start'
      ]
    ]
    
    for t in test:
        print(run(t))

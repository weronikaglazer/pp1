#pierwsza funkcja oblicza wprowadzone w postaci ONP wyrazenie 
#druga funkcja konweruje wyrazenie w notacji regularnej do ONP i oblicza je

def evaluate_RPN(string):
    tokens = []
    stack = []

    for char in string:
        tokens.append(char)

    for token in tokens:
        if token.isdigit():
            stack.append(token)
        elif token in ["+","-","/","*"]:
            value2 = int(stack.pop())
            value1 = int(stack.pop())
            if token == "+":
                stack.append(value1+value2)
            elif token == "-":
                stack.append(value1-value2)
            elif token == "*":
                stack.append(value1*value2)
            elif token == "/":
                stack.append(value1/value2)
        elif token == "=":
            result = stack.pop()
        
    result_line = "The final result is " + str(result)
    return result_line


def convert_to_RPN(string):
    result = str(eval(string))
    stack = []
    output = []
    tokens = []

    for char in string:
        tokens.append(char)

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in ["+","-","/","*"]:
            if len(stack) == 0:
                stack.append(token)
            elif stack[-1] == "(":
                stack.append(token)
            else:
                while len(stack) != 0 and stack[-1] != "(":
                    output.append(stack.pop())
                stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()

    while len(stack) != 0:
        output.append(stack.pop())

    final_output = " ".join(output)
    rpn_line = "RPN result: " + final_output + "\n"
    eval_line = "Calculated: " + result
    final = rpn_line + eval_line

    return final
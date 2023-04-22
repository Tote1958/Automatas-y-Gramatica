def solve(string):
    numbers = []
    operators = []
    i = 0
    while i < len(string):
        if string[i].isdigit():
            num = ""
            while i < len(string) and string[i].isdigit():
                num += string[i]
                i += 1
            numbers.append(int(num))
        elif string[i] == "*":
            operators.append(string[i])
            i += 1
        elif string[i] == "+":
            operators.append(string[i])
            i += 1
        else:
            i += 1
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i+1]
        elif operators[i] == "*":
            result *= numbers[i+1]
    return result

def split_op(string):
    terms = string.split('+')
    total = 0
    print(terms)
    resolved = []
    for i in terms:
        n = 0
        terms[n] = str(solve(i))
        n = n + 1
        resolved.append(str(solve(i)))
    for i in resolved: 
        total = total + int(i)
    return total



operation = str(input('Ingrese una operación: '))
print(split_op(operation))

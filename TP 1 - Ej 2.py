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

operation = str(input('Ingrese una operación: '))
print(solve(operation))
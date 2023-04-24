def checker(line):
    checker = int(0)
    parts = line.split('.')
    if len(parts) == 4:
        for part in parts:
            if part.isdigit():
                if 0 <= int(part) <= 255:
                    checker += 1
    if checker == 4:
        checker = 0
        print(line, ' Es una dirección IPv4 válida')
    else:
        print(line, ' No es una dirección IPv4 válida.')

with open('Ej_c.txt') as file:
    line = file.readlines()
    for i in line:
        checker(i)
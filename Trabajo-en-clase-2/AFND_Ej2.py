def veryfier (string):
    if string[0] == ' ':
        string = string[1:]
    status = 1
    for i in string:
        print(status)
        if status == 1:
            if i == 'a':
                status = 2
            elif i == 'b':
                status = 4
            elif i == ' ':
                status = 5
        elif status == 2:
            if i == 'a':
                status = 3
            else:
                print('La cadena es inválida.')
                break
        elif status == 3 or status == 4:
            status = 5
        elif status == 5:
            if i == 'a':
                status = 6
            elif i == 'b':
                status = 7
            elif i == ' ':
                status = 1
        elif status == 6 or status == 8:
            status = 9
        elif status == 7:
            if i == 'b':
                status = 8
            else:
                print('Cadena incorrecta.')
                break
        elif status == 9:
            print('Cadena correcta.')
            break
    if status == 9 or status == 5:
        print('Cadena Correcta!!')
    else:
        print('Cadena incorrecta...')




string = str(input('Ingrese una cadena: '))
veryfier(string)

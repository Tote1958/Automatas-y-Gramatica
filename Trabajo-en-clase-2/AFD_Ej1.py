def veryfier (string):
    for i in string:
        if i == 'a':
            pass
        elif i == 'b':
            pass
        else: 
            return False
    return True

string = str(input('Ingrese una cadena: '))
print(veryfier(string))
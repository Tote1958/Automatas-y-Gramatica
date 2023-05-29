import re


def get_emails():
    with open("/home/tote/Automatas-y-Gramatica/TPN1/Ej_a.txt","r") as f:
        email_list = f.readlines()
        
    emails = []
    for i in email_list:
        split = i.split("\n")
        char = split[0]
        emails.append(char)
    return emails

def has_at(list_of_emails):  
    at = "@"
    emails = []
    for i in list_of_emails:
        if re.search(at, i):
            emails.append(i)
        else:
            print(f'La cadena {i} no contiene @, por lo tanto no puede ser un email valido')
    return emails


validate = r'([a-z])([a-zA-Z0-9]|_|\.|\-)*@(clarin|hotmail|gmail|apple|outlook)\.com(\.(es|ar|us|cl|co))?'

emails = has_at(get_emails())
for i in emails:
    if re.fullmatch(validate, i):
        print(f'{i} es un email')
    else:
        print(f'{i} no es un email')

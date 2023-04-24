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
            print(f'La cadena {i} no contiene @ por lo tanto no puede ser un email valido')
    return emails


def validate_email(emails):
    for i in emails:
        n = 0                                                                   #Estoy encarando bien este ej en general?                                                           # O habria que hacerlo con automatas y los diagramas?
        email = i.split("@")                                                    #Podria usar re.compile
        dom = email[(n + 1)].split(".")
        for index in range(3):
            email.append(dom[index])
        email.pop(n + 1)
        n += 1

        print(email)

        is_email = True
        if re.fullmatch(name, email[0]):
            pass
        else:
            is_email = False
        if re.fullmatch(dominios, email[1]):
            pass
        else:
            is_email = False

        if re.fullmatch('com', email[2]):
            pass
        else:
            is_email = False
            
        if re.fullmatch(countries, email[3]):
            pass
        else:
            is_email = False
            
        if is_email == True:
            emails_are_emails.append(True)
        else:
            emails_are_emails.append(False)

    #print(emails_are_emails) 

    for i in range(len(emails)):
        if emails_are_emails[i] == True:
            print(f'La cadena {emails[i]} es un email valido')
        elif emails_are_emails[i] == False:
            print(f'La cadena {emails[i]} es un email invalido')

name = '([a-z])([0-9]|_|.|-)*'                                             # [a-z] no es de la a hasta la z, son todas las letras ASCII, por eso toma el #, ? etc.
dominios = '(clarin)|(hotmail)|(gmail)|(apple)|(outlook)'
countries = '(es)|(ar)|(us)|(cl)|(co)'
emails_are_emails = []

emails = has_at(get_emails())
#print(emails)
validate_email(emails)

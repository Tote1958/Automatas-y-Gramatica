import re


def get_links():
    with open("/home/tote/Automatas-y-Gramatica/TPN1/Ej_b.txt","r") as f:
        links_list = f.readlines()
        
    links = []
    ind = 0
    for i in links_list:
        split = i.split("\n")
        char = split[0]
        links.append(char)
        ind = ind + 1
    links.pop(ind - 1)
    return links




links = get_links()
print(links)
web = '(http|https)?(://)?(www\.)([a-z]|[A-Z]|[0-9])*(\.)(com)(/)*'

n = 0
for i in links:
    is_link = re.fullmatch(web, i)
    if is_link:
        print(f'La cadena {links[n]} es un link')
    else:
        print(f'La cadena {links[n]} no es un link')
        
    n = n + 1
    

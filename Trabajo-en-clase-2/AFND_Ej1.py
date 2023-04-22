
exp = str(input("Ingrese la expresion: "))
exp_slice = []
for i in range(len(exp)):
    exp_slice.append(exp[i:(i+1)])


error = False
for i in range(len(exp_slice)):
    if exp_slice[i] != "a" and exp_slice[i] != "b":
        error = True
    elif len(exp_slice) == 0:
        error = False

if error == True:
    print("Error")
elif error == False:
    print("La expresion es correcta.")

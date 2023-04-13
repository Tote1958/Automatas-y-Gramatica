exp = str(input("Ingrese la expresion: "))
n_global = 0
n = 0
error = False

exp_slice = []
for i in range(len(exp)):
    exp_slice.append(exp[i:(i+1)])

print(exp_slice)
print(len(exp_slice))

for i in range(len(exp_slice)):
    print("iteracion", i)
    if ((i+1) <= (len(exp_slice))):
        if(exp_slice[i] == "a" and exp_slice[i+1] == "a"):
            i = (i+2)
            pass
    elif exp_slice[i] == "b":
        i = (i+1)
        pass
    elif len(exp_slice) == 0:
        error = False
        break
    else:
        error = True
        break
    if i >= len(exp_slice):
        break

    n = n + 1
print("n= ", n)

"""

if len(exp_slice) > n:
    n = n - 1
    for i in range(len(exp_slice)):
        print("iteracion", n)
        if ((n+1) <= (len(exp_slice))):
            if(exp_slice[n] == "b" and exp_slice[n+1] == "b"):
                i = (n+2)
                pass
        elif exp_slice[n] == "a" and (exp_slice[n+1] == "b" or exp_slice[n+1] == exp_slice[0]):
            n = (n+1)
            pass
        elif len(exp_slice) == 0:
            error = False
            break
        else:
            error = True
            break
        if i >= len(exp_slice):
            break

        n = n + 1
    print("n= ", n)


"""





if error == False: print("Anduvo")
if error == True: print("Algo fallo")
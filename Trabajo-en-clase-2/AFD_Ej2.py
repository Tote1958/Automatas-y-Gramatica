exp = str(input("Ingrese la expresion: "))
state = "A"
error = False
dict = {("A","a"): "B", ("A","b"): "C",
 ("B","a"): "D", ("B","b"): "C", ("C","a"): "B",
  ("C","b"): "C", ("D","a"): "D", ("D","b"): "C",}

print(len(exp))
if len(exp) == 0:
    error = True
for i in exp:
    state = dict[(state, i)]
    print(state)
    if (i != "a") and (i != "b"):
        error = True

if ((state == "A") or (state == "B") or (state == "C") or (state == "D")) and (error == False):
    print("El estado final es:", state)

elif error == True:
    print("Algo ha salido mal")
    
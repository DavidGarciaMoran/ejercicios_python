
asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
dict = {}
for i in asignaturas:
    nota = input("Dime tu nota en " + str(i) +":")
    dict[i] = nota

print("Estas son tus notas \n")

for i in dict:
    print(f"En {i} sacaste un {dict[i]}".format(i ,dict[i]))
    

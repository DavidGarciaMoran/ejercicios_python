file = open('myfile.txt', 'w')
text = "Hola mundo"
file.write(text)
file.close()
file = open('myfile.txt', 'a')
file.write(text)
file.close()

compra = {'a','b','c'}
f = open("Lista.txt", "w")
for item in compra:
    f.write(item)
f.close()
lista =[]
pregunta = 1
while pregunta == 1 :
	nota = str(input("Ingrese un nota: "))
	lista.append(nota)
	pregunta = int(input("Desea ingresar otra nota?  1 = si 2 = no R/:"))
	
notas=("\n").join(lista)
f = open("notasguardadas.txt", "w")
f.write(str(notas))
f.close()





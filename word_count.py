import sys


if len(sys.argv) < 2:
    print("Debe escribir el nombre del archivo")
else:
    with open(sys.argv[1], "r") as archivo:
        texto = archivo.read()
        
        palabras = len(set(texto.split(" ")))
        print(f"El número de palabras distintas dentro del texto {sys.argv[1]} son: {palabras}")
        letras = len(set(texto))
        
        print (f"El número de caracteres distintos dentro del texto {sys.argv[1]} son: {letras}")
        #print(set(texto))
        

import os

print("descarga videos de xvideos")
xv=raw_input('ingrea el link de dicho video: ')


os.system("wget -O texto.txt "+xv)

palabra = 'setVideoUrlHigh'
ocurrencias = filter(lambda line: palabra in line, open('texto.txt').readlines())

print ocurrencias
print("a hora copia el link que aparese en la terminal y abrelo directamnete en tu navegador de internet ya sea firefoz o chrome y descargalo ")




print ("listo cochinote") 

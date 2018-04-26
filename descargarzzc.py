import os
print ("descargar videos de pornub.com script con el mismo funcionamiento de descargaxv.py programado por Big Boss")
zzc=raw_input("ingrese el link del video de zzcartoon.com")
os.system('wget -O tex.txt '+zzc)

palabra='video_url:'

ocurrecincia = filter(lambda line: palabra in line,open('tex.txt').readlines())
print ocurrecincia
print "ingonra todo menos los link que te arroje la terminal" 
input('enter para finalizar')
os.system('rm tex.txt')
exit()


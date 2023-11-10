from filelock import FileLock
from os import getpid
from time import sleep,time

debut = time()
verrou = FileLock("test.txt")

print("Je suis", getpid(), "qui va prendre le verrou")
verrou.acquire()
print("Je suis", getpid(), "qui a pris le verrou")

print("Je fais une pause ! Je bloque la ressource")
sleep(20)

fin = time()
duree = round(fin - debut,2)

print("Fin du processus, la ressource est libérée ! Durée du processus :",duree)
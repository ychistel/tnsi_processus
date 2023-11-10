from filelock import FileLock
from os import getpid
from time import sleep,time

t = 5
debut = time()
# on crée 2 verrous
verrou_1 = FileLock("test_1.txt")
verrou_2 = FileLock("test_2.txt")

# on demande la ressource 1
print("Je suis", getpid(), "qui va prendre la ressource 1")
verrou_1.acquire()
print("Je suis", getpid(), "qui a pris la ressource 1")
print("Je fais une pause ! Je bloque la ressource 1")
sleep(t)

# on libère la ressource 1
print("je libère la ressource 1")
verrou_1.release()
sleep(t)

# on demande la ressource 2
print("Je suis", getpid(), "qui va prendre la ressource 2")
verrou_2.acquire()
print("Je suis", getpid(), "qui a pris la ressource 2")
print("Je fais une pause ! Je bloque la ressource 2")
sleep(t)

# on libère la ressource 2
print("je libère la ressource 2")
verrou_2.release()
sleep(t)

# calcul de la durée du processus
fin = time()
duree = round(fin - debut,2)

print("Fin du processus! On libère les ressources. Durée du processus :",duree)
from filelock import FileLock
from os import getpid
from time import sleep

verrou = FileLock("test.txt")

print("Je suis", getpid(), "qui va prendre le verrou")
verrou.acquire()
print("Je suis", getpid(), "qui a pris le verrou")
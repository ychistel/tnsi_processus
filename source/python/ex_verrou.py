from filelock import FileLock
from os import getpid

le_verrou = FileLock("test.txt")
le_verrou.acquire()

print("je suis",getpid())

while True:
    pass
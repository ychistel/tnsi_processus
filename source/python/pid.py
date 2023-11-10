from os import getpid,getppid,kill
from time import sleep

mon_pid = getpid()
parent_pid = getppid()

print("Je suis",mon_pid)
print("mon parent est",parent_pid)

"""
while True:
    pass
"""

sleep(5)
print("fin du processus")

#kill(5512,9)
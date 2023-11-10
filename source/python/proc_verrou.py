from filelock import FileLock

FNAME1 = "verrou1.lock"
FNAME2 = "verrou2.lock"

verrou_1= FileLock("test.txt")
#verrou_2 = FileLock(FNAME2)

verrou_1.acquire()
with open("test.txt",mode='a') as f:
    f.write('verrou 1 inactif \n')
verrou_1.release()

"""
verrou_1.acquire()
    #verrou_2.acquire()

with open("test.txt",mode='a') as f:
    f.write('verrou 1 actif\n')

    #verrou_2.release()
verrou_1.release()
"""
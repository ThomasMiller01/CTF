import tarfile
import os

try:
    os.mkdir("./like1000/extracted")
except:
    pass
tar = tarfile.open("./like1000/1000.tar")

for i in range(999, 0, -1):
    tar.extractall(path="./like1000/extracted/")
    tar.close()
    tar = tarfile.open("./like1000/extracted/" + str(i) + ".tar")

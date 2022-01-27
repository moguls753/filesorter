# a filesorter to sort all incoming files to ~/Downloads
import os

os.chdir("/home/eike/Downloads")
for file in os.listdir():
    print(file)


import os
import random

filelist = [filename.strip(".jpg") for filename in os.listdir('./images')]
length = len(filelist)
modeltest = sorted(filelist)
print("Test: "+str(len(modeltest)))


with open("modeltest.txt", "w") as te:
	for text in modeltest:
		te.write(text + "\n")

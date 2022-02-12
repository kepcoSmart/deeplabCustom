import os
import random

filelist = [filename.strip(".png") for filename in os.listdir('./labels')]
random.shuffle(filelist)
length = len(filelist)
pa1 = int(length*0.6)
pa2 = pa1 + int(length*0.2)
train = filelist[:pa1]
val = filelist[pa1:pa2]
modeltest = filelist[pa2:]
print("Train: "+str(len(train)), " / Validation: "+str(len(val)), " / Test: "+str(len(modeltest)))


with open("train.txt", "w") as tr:
	for text in train:
		tr.write(text + "\n")
with open("val.txt", "w") as va:
	for text in val:
		va.write(text + "\n")
with open("modeltest.txt", "w") as te:
	for text in modeltest:
		te.write(text + "\n")

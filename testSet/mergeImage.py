import os
import cv2
import math
from PIL import Image

# Custom parameters
originalPath = 'imagesTest'
originalList = [i for i in os.listdir(originalPath)]
originalImage = cv2.imread(originalPath+'/'+originalList[0])
imageSize = 224
imageX = math.floor(originalImage.shape[0]/imageSize)
imageY = math.floor(originalImage.shape[1]/imageSize)
imageNumber = imageX * imageY
filePath = './visualization/segmentation_results'
imagePattern = 'image.png'
labelPattern = 'prediction.png'

# Custom folders
os.mkdir("mergedImages")          # Predicted full images

imageList = [i for i in os.listdir(filePath) if imagePattern in i]
imageList = sorted(imageList)
labelList = [l for l in os.listdir(filePath) if labelPattern in l]
labelList = sorted(labelList)
# print(len(filelist))
# with open("ttt.txt", "w") as tr:
#    for text in fileList:
#        tr.write(text + "\n")

n = 0
for imageFile in range(0, len(originalList)):
#    print(fileList[imageFile])
    fullImage = Image.new('RGB', (imageY*imageSize, imageX*imageSize))
    fullLabel = Image.new('RGB', (imageY*imageSize, imageX*imageSize))
    for i in range(0, imageX*imageSize, imageSize):
        for j in range(0, imageY*imageSize, imageSize):
            subImage = Image.open(filePath+'/'+imageList[n])
            fullImage.paste(subImage, (j, i))
            subLabel = Image.open(filePath+'/'+labelList[n])
            fullLabel.paste(subLabel, (j, i))
            n = n+1
    resultImage = Image.blend(fullImage, fullLabel, alpha=0.5)
    resultImage.save('./mergedImages/'+str(imageFile).zfill(5)+'.png')
    print(str(round((imageFile/len(originalList)*100),2))+'%')
#    fullImage.save('./mergedImages/'+str(imageFile).zfill(5)+'.jpg')
#    fullLabel.save('./mergedImages/'+str(n).zfill(3)+'.png')

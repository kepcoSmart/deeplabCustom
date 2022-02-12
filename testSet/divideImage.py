import os
import cv2
from PIL import Image

# Custom parameters
imageSize = 224
# imageX = 10
# imageY = 10
# imageNumber = 100
imagePath = 'imagesTest'
# labelPath = 'labelsTest'

# Custom folders
os.mkdir("images")          # Sub-images
os.mkdir("labels")          # Sub-labels
# os.mkdir("groundTruths")    # Full images with the associated label information

imageList = [i for i in os.listdir(imagePath)]
imageList = sorted(imageList)
# labelList = [l for l in os.listdir(labelPath)]
# labelList = sorted(labelList)
# print(len(filelist))
# with open("ttt.txt", "w") as tr:
#    for text in fileList:
#        tr.write(text + "\n")

n = 0
for imageFile in range(0, len(imageList)):
#    print(str(imageFile).zfill(5))
    image = cv2.imread(imagePath+'/'+imageList[imageFile])
    for r in range(0, image.shape[0]-imageSize, imageSize):
        for c in range(0, image.shape[1]-imageSize, imageSize):
            cv2.imwrite('./images/ds_'+str(n).zfill(5)+'.jpg', image[r:r+imageSize, c:c+imageSize, :])
            cv2.imwrite('./labels/ds_'+str(n).zfill(5)+'.png', image[r:r+imageSize, c:c+imageSize, 0])
            n = n+1
    print(str(round((imageFile/len(imageList)*100),2))+'%')

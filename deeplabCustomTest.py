import os
import sys
import random
import time
import shutil

# Step 0. Add libraries
os.chdir("./models/research")
os.system("export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim")

# Step 1. Divide images
print("Step 1. Divide images ..........")
os.chdir("./deeplab/datasets/testSet")
os.system("python divideImage.py")
print("Step 1. Divide images ..........Done")

# Step 2. Prepare datasets
print("Step 2. Prepare datasets ..........")
os.makedirs("tfrecord")
os.system("python partitionData.py")
print("Step 2. Prepare datasets ..........Done")

# Step 3. Generate tfRecord foramt
print("Step 3. Generate tfRecord format ..........")
os.chdir("..")
os.system("python build_voc2012_test.py")
print("Step 3. Generate tfRecord format ..........Done")

# Step 4. Test segmentation model
print("Step 4. Test segmentation model ..........")
os.chdir("..")
os.system("python vis_test.py --logtostderr --model_variant='xception_65' --max_number_of_iterations=1")
print("Step 4. Test segmentation model ..........Done")

# Step 5. Merge images
print("Step 5. Merge images ..........")
os.chdir("./datasets/testSet")
os.system("python mergeImage.py")
shutil.rmtree("labels")
print("Step 5. Merge images ..........Done")

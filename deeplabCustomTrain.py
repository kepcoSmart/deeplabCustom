import os
import sys
import random
import time

# Step 0. Add libraries
os.chdir("./models/research")
os.system("export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim")

# Step 1. Divide images
print("Step 1. Divide images ..........")
os.chdir("./deeplab/datasets/trainSet")
os.system("python divideImage.py")
print("Step 1. Divide images ..........Done")

# Step 2. Prepare Dataset
print("Step 2. Prepare Dataset ..........")
os.makedirs("tfrecord")
os.system("python partitionData.py")
print("Step 2. Prepare Dataset ..........Done")

# Step 3. Generate tfRecord foramt
print("Step 3. Generate tfRecord format ..........")
os.chdir("..")
os.system("python build_voc2012_data.py")
print("Step 3. Generate tfRecord format ..........Done")

# Step 4. Train segmentation model
print("Step 4. Train segmentation model ..........")
os.chdir("..")
os.system("python train.py --logtostderr --model_variant='xception_65'")
print("Step 4. Train segmentation model ..........Done")

# Step 5. Test segmentation model
print("Step 5. Test segmentation model ..........")
os.system("python vis.py --logtostderr --model_variant='xception_65' --max_number_of_iterations=1")
print("Step 5. Test segmentation model ..........Done")

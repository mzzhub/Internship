# -*- coding: utf-8 -*-
"""ObjectDetection YOLO.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZWnqgFMLAPGb1lzpoQQsBfG5Xqe655Wu

# **Load Raw Materials**
* only for local execution
"""

# !pip install ultralytics opencv-python-headless

# ! pip install torch torchvision torchaudio matplotlib

# ! git clone https://github.com/ultralytics/yolov5.git

# !pip install -r /content/yolov5/requirements.txt

"""# **Build Model**"""

import torch
import cv2
# from pathlib import Path
# import matplotlib.pyplot as plt

model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained = True)

image_path = "/content/drive/MyDrive/Colab Notebooks/Deep Learning/Object dection/images/dog_bike_car.jpg"
image = cv2.imread(image_path)

# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.axis("off")
# plt.show()

image

result = model(image_path)

result.show()

result.print()

"""# **More Tests**"""

image02 = "/content/drive/MyDrive/Colab Notebooks/Deep Learning/Object dection/images/Screenshot 2024-11-09 232638.png"
result02 = model(image02)
result02.show()

street01_path = "/content/drive/MyDrive/Colab Notebooks/Deep Learning/Object dection/images/street01.webp"
street01 = model(street01_path)
street01.show()

model("/content/drive/MyDrive/Colab Notebooks/Deep Learning/Object dection/images/table.webp").show()

model("/content/drive/MyDrive/Colab Notebooks/Deep Learning/Object dection/images/officetable.jpg").show()
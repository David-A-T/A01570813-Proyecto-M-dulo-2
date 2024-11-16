from ultralytics import YOLO # YOLO Model
import os # FIle Handling

# LOAD MODEL IF ALREADY RE-TRAINED #
from ultralytics import YOLO
import torch
model = YOLO("best.pt")

print('Enter Image Path (use \\\') :')
image = input()
#image=(r)

model = model.to("cpu")  # Ensure the model is set to CPU
results = model.predict(image, device="cpu")
#print(results)
results[0].show()
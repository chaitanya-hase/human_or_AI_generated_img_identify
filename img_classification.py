
from transformers import AutoModelForImageClassification, AutoFeatureExtractor
from PIL import Image
import torch

model_name = "ideepankarsharma2003/AI_ImageClassification_MidjourneyV6_SDXL"

model = AutoModelForImageClassification.from_pretrained(model_name)
feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)

from google.colab import files

# Prompt user to upload image(s)
uploaded = files.upload()  

# Get the uploaded image filename
image_path = next(iter(uploaded))

# Open image and convert to RGB

image = Image.open(image_path).convert("RGB")

# Pass as a list of images
inputs = feature_extractor(images=[image], return_tensors="pt")

model.eval()
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_label = logits.argmax(-1).item()

id2label = {0: "ai_gen", 1: "human"}
print("Predicted label:", id2label[predicted_label])

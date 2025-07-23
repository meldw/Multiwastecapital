
import os
from transformers import pipeline, AutoImageProcessor, AutoModelForImageClassification
from PIL import Image


hf_token = os.getenv("HF_TOKEN")


def classify_image_from_url(image_url, token=hf_token):
    pipe = pipeline("image-classification", model="youssefabdelmottaleb/Garbage-Classification-SWIN-Transformer", token=token)
    result = pipe(image_url)
    return result

def classify_image_from_file(image_path, token=hf_token):
    processor = AutoImageProcessor.from_pretrained("youssefabdelmottaleb/Garbage-Classification-SWIN-Transformer", token=token)
    model = AutoModelForImageClassification.from_pretrained("youssefabdelmottaleb/Garbage-Classification-SWIN-Transformer", token=token)

    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    label = model.config.id2label[predicted_class_idx]
    return label



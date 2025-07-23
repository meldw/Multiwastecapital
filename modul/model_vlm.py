'''
import os
from transformers import pipeline, AutoImageProcessor, AutoModelForImageClassification
from PIL import Image


hf_token = os.getenv("HF_TOKEN")


def classify_image_from_url(image_url, token=hf_token):
    pipe = pipeline("image-classification", model="yangy50/garbage-classification", token=token)
    result = pipe(image_url)
    return result

def classify_image_from_file(image_path, token=hf_token):
    processor = AutoImageProcessor.from_pretrained("yangy50/garbage-classification", token=token)
    model = AutoModelForImageClassification.from_pretrained("yangy50/garbage-classification", token=token)

    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    label = model.config.id2label[predicted_class_idx]
    return label

'''
import os
import gdown
import pickle

MODEL_PATH = "modul/modelllm.pkl"
DRIVE_FILE_ID = "1n8f9yuMOBleuoAGhIgpta5MsQSynxzrt"  # Ganti dengan ID-mu

# Download dari Google Drive kalau belum ada
def download_model_if_needed():
    if not os.path.exists(MODEL_PATH):
        print("Downloading model from Google Drive...")
        url = "https://drive.google.com/file/d/1n8f9yuMOBleuoAGhIgpta5MsQSynxzrt/view?usp=sharing"
        gdown.download(url, MODEL_PATH, quiet=False)

# Load model
def load_model():
    download_model_if_needed()
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model

# Load once and reuse
model = load_model()

# Prediction function
def classify_image_from_file(image_file):
    # Load image, process, then:
    # e.g., result = model.predict(image_data)
    # (contoh dummy):
    return model.predict([image_file])


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
'''
'''
import torch
import torch.nn as nn
import os
import gdown

# 👇 Langsung taruh definisi model di sini
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc1 = nn.Linear(100, 50)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        return self.fc2(x)

MODEL_PATH = "modul/modelllm.pkl"
DRIVE_FILE_ID = "1n8f9yuMOBleuoAGhIgpta5MsQSynxzrt"  # Ganti dengan ID kamu

def download_model_if_needed():
    if not os.path.exists(MODEL_PATH):
        print("Downloading model from Google Drive...")
        url = "https://drive.google.com/uc?id=1n8f9yuMOBleuoAGhIgpta5MsQSynxzrt"
        gdown.download(url, MODEL_PATH, quiet=False)

def load_model():
    download_model_if_needed()
    model = MyModel()
    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
    model.eval()
    return model
'''
# app.py
import os
import torch
import torch.nn as nn
import gdown
from fastapi import FastAPI, UploadFile, File
from PIL import Image
from io import BytesIO
import torchvision.transforms as transforms

app = FastAPI()

# Model definisi
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc1 = nn.Linear(100, 50)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        return self.fc2(x)

MODEL_PATH = "modelllm.pkl"
DRIVE_FILE_ID = "1n8f9yuMOBleuoAGhIgpta5MsQSynxzrt"

def download_model_if_needed():
    if not os.path.exists(MODEL_PATH):
        url = f"https://drive.google.com/uc?id={DRIVE_FILE_ID}"
        gdown.download(url, MODEL_PATH, quiet=False)

def load_model():
    download_model_if_needed()
    model = MyModel()
    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
    model.eval()
    return model

model = load_model()

# Preprocessing sesuai input model kamu
transform = transforms.Compose([
    transforms.Resize((10, 10)),  # contoh ukuran input, sesuaikan dengan model kamu
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])
])

@app.post("/classify-image")
async def classify_image(file: UploadFile = File(...)):
    # Baca gambar dari upload file
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert("RGB")

    # Preprocess gambar ke tensor
    input_tensor = transform(image).unsqueeze(0)  # batch size 1

    # Prediksi dengan model
    with torch.no_grad():
        output = model(input_tensor)
        predicted_class_idx = output.argmax(dim=1).item()

    # Contoh label, sesuaikan dengan model kamu
    labels = ["class_0", "class_1", "class_2", "class_3", "class_4",
              "class_5", "class_6", "class_7", "class_8", "class_9"]

    predicted_label = labels[predicted_class_idx]

    return {"label": predicted_label}


model = load_model()



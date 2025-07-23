from transformers import pipeline

# Inisialisasi pipeline dengan model dari Hugging Face
pipe = pipeline(
    "text-generation",
    model="satvikag/chatbot",
    max_new_tokens=100,
    do_sample=True,
    temperature=0.7,
)

def get_bot_reply(user_input):
    prompt = user_input
    result = pipe(prompt)
    reply = result[0]["generated_text"].replace(prompt, "").strip()
    return reply

'''
import os
import torch
import torch.nn as nn
import gdown
from PIL import Image
from io import BytesIO
import requests
import torchvision.transforms as transforms

# ======= MODEL DEFINISI =======
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        # contoh layer, sesuaikan dengan modelmu
        self.fc1 = nn.Linear(100, 50)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        return self.fc2(x)

# ======= MODEL PATH & DOWNLOAD =======
MODEL_PATH = "modelllm.pkl"
DRIVE_FILE_ID = "1n8f9yuMOBleuoAGhIgpta5MsQSynxzrt"  # ganti sesuai ID kamu

def download_model_if_needed():
    if not os.path.exists(MODEL_PATH):
        url = "https://drive.google.com/uc?id=1n8f9yuMOBleuoAGhIgpta5MsQSynxzrt"
        gdown.download(url, MODEL_PATH, quiet=False)

# Load model sekali saat modul di-import
def load_model():
    download_model_if_needed()
    model = MyModel()
    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
    model.eval()
    return model

model = load_model()

# ======= TRANSFORM IMAGE =======
transform = transforms.Compose([
    transforms.Resize((10, 10)),  # sesuaikan ukuran input model kamu
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])
])

# ======= FUNSI UTAMA =======

def classify_image_from_url(image_url, token=None):
    """
    Download image dari URL, lalu klasifikasi dengan model PyTorch.
    Token diabaikan supaya signature tetap sama.
    """
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content)).convert("RGB")
    input_tensor = transform(image).unsqueeze(0)  # batch size 1

    with torch.no_grad():
        output = model(input_tensor)
        predicted_class_idx = output.argmax(dim=1).item()

    # Contoh label, sesuaikan dengan label asli modelmu
    labels = ["class_0", "class_1", "class_2", "class_3", "class_4",
              "class_5", "class_6", "class_7", "class_8", "class_9"]

    predicted_label = labels[predicted_class_idx]
    return predicted_label

def classify_image_from_file(image_path, token=None):
    """
    Baca gambar dari file lokal, klasifikasi dengan model PyTorch.
    Token diabaikan supaya signature tetap sama.
    """
    image = Image.open(image_path).convert("RGB")
    input_tensor = transform(image).unsqueeze(0)  # batch size 1

    with torch.no_grad():
        output = model(input_tensor)
        predicted_class_idx = output.argmax(dim=1).item()

    # Contoh label, sesuaikan dengan label asli modelmu
    labels = ["class_0", "class_1", "class_2", "class_3", "class_4",
              "class_5", "class_6", "class_7", "class_8", "class_9"]

    predicted_label = labels[predicted_class_idx]
    return predicted_label
'''

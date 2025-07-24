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
from transformers import pipeline

# Inisialisasi pipeline sekali saja di global scope supaya tidak reload berulang-ulang
pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen1.5-1.8B-Chat",
    max_new_tokens=100,
    do_sample=True,
    temperature=0.7,
)

def get_bot_reply(user_input):
    messages = [{"role": "user", "content": user_input}]
    result = pipe(messages)
    full_text = result[0]["generated_text"]

    # Bersihkan output supaya hanya balasan chatbot yang tersisa
    reply = full_text
    for msg in messages:
        reply = reply.replace(msg["content"], "").strip()
    return reply

if __name__ == "__main__":
    # Contoh penggunaan
    user_text = "Who are you?"
    print("User:", user_text)
    print("Bot:", get_bot_reply(user_text))

'''
'''
# app.py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

MODEL_ID = "meta-llama/Meta-Llama-3-8B"

# Load tokenizer dan model
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16,
    device_map="auto"
)

# Siapkan pipeline untuk text generation
chat = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Fungsi chat loop
def chat_with_bot():
    print("🤖 LLaMA 3 Chatbot (meta-llama/Meta-Llama-3-8B)")
    print("Ketik 'exit' untuk keluar.\n")
    while True:
        user_input = input("🧑 Kamu: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Bye!")
            break

        # Format prompt gaya LLaMA 3 (simple version)
        prompt = f"<|user|>\n{user_input}\n<|assistant|>\n"
        response = chat(prompt, max_new_tokens=256, do_sample=True, temperature=0.7)
        bot_output = response[0]['generated_text'].split("<|assistant|>")[-1].strip()
        print(f"🤖 Bot: {bot_output}\n")

if __name__ == "__main__":
    chat_with_bot()
'''
'''
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model dan tokenizer sekali saja
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen1.5-1.8B-Chat", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen1.5-1.8B-Chat", trust_remote_code=True, device_map="auto")

# Template sistem & beberapa pertanyaan sebelumnya
base_messages = [
    {"role": "system", "content": "You are a helpful assistant specialized in waste management, garbage classification, and sustainable investment."},
    
    {"role": "user", "content": "Apa yang dimaksud dengan klasifikasi sampah dan mengapa penting dalam pengelolaan multiwaste?"},
    {"role": "assistant", "content": "Klasifikasi sampah adalah proses pemisahan sampah berdasarkan jenisnya seperti organik, anorganik, B3, dan daur ulang. Ini penting agar pengelolaan lebih efisien dan ramah lingkungan."},

    {"role": "user", "content": "Berikan contoh bagaimana AI bisa membantu klasifikasi sampah rumah tangga."},
    {"role": "assistant", "content": "AI dapat digunakan untuk mengenali jenis sampah dari gambar menggunakan model vision, lalu otomatis mengarahkan sampah ke kategori yang sesuai."},
    
]

# Fungsi yang bisa dipanggil sebagai endpoint
def get_bot_reply(user_input):
    # Tambahkan pertanyaan user terbaru
    messages = base_messages + [{"role": "user", "content": user_input}]
    
    # Tokenisasi dan format
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_tensors="pt"
    ).to(model.device)

    # Generate respon
    outputs = model.generate(
        **inputs,
        max_new_tokens=300,
        do_sample=True,
        temperature=0.7,
        top_p=0.95
    )

    # Ambil hanya output dari jawaban model
    response = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[-1]:],
        skip_special_tokens=True
    )
    return response


# --- Testing lokal ---
if name == "main":
    print("Qwen Assistant (topik: sampah, AI, investasi)\nKetik 'exit' untuk keluar.\n")
    while True:
        user_input = input("🧑 Kamu: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            break
        reply = get_bot_reply(user_input)
        print("🤖 Bot:", reply)
        '''

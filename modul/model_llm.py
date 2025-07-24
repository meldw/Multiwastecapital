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

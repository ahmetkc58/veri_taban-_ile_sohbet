import google.generativeai as genai
from api_key import get_api_key
import re
import os

# prompt.txt dosyasından prompt içeriğini oku
def get_prompt_from_file():
    dosya_yolu = os.path.join(os.path.dirname(__file__), 'prompt.txt')
    with open(dosya_yolu, 'r', encoding='utf-8') as f:
        return f.read()

# API anahtarını al ve yapılandır
api_key = get_api_key()
genai.configure(api_key=api_key)

def send_prompt_to_gemini(question):
    """
    prompt.txt dosyasından promptu okur, verilen soruyla birlikte Gemini API'ye gönderir, yanıtı döndürür.
    """
    prompt = get_prompt_from_file()
    model = genai.GenerativeModel('models/gemini-2.0-flash')
    response = model.generate_content([prompt, question])
    return response.text

def ilk_ve_son_satiri_sil(metin):
    satirlar = metin.splitlines()
    if len(satirlar) > 2:
        satirlar = satirlar[1:-1]
    elif len(satirlar) == 2:
        satirlar = [satirlar[1]]
    elif len(satirlar) == 1:
        satirlar = []
    return "\n".join([s.strip() for s in satirlar if s.strip()])

# Artık ana akış main.py'de, bu dosya sadece fonksiyon sağlar.
# Dosya tabanlı iletişim ve __main__ bloğu kaldırıldı.




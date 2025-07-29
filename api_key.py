import os
from dotenv import load_dotenv

# .env dosyasından anahtarı yükle
load_dotenv()
 
def get_api_key():
    return os.getenv("GOOGLE_API_KEY")
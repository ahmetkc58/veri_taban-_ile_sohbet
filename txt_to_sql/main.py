from prompt import send_prompt_to_gemini, ilk_ve_son_satiri_sil
from sql import sql_sorgusu_calistir

if __name__ == "__main__":
    while True:
        question = input("Soru girin (çıkmak için 'q' yazın): ")
        if question.lower() == "q":
            break
        yanit = send_prompt_to_gemini(question)
        temiz_sorgu = ilk_ve_son_satiri_sil(yanit)
        print("Sorgu sonucu:")
        sql_sorgusu_calistir(temiz_sorgu)

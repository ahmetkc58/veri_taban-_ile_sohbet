import gradio as gr
from prompt import send_prompt_to_gemini, ilk_ve_son_satiri_sil
from sql import sql_sorgusu_calistir
import random
import os

def gradio_akisi(question):
    try:
        yanit = send_prompt_to_gemini(question)
        temiz_sorgu = ilk_ve_son_satiri_sil(yanit)
        sonuc = sql_sorgusu_calistir(temiz_sorgu, return_df=True)
        return temiz_sorgu, sonuc
    except Exception as e:
        return f"Hata: {str(e)}", None

def gemini_soru_uret():
    dosya_yolu = os.path.join(os.path.dirname(__file__), "prompt2.txt")
    with open(dosya_yolu, "r", encoding="utf-8") as f:
        prompt = f.read()
    return send_prompt_to_gemini(prompt)

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # Doğal Dilden MSSQL Sorgu Sistemi
    Kullanıcı dostu arayüz ile doğal dilde sorunuzu yazın, Gemini ile MSSQL sorgusu oluşturulsun ve sonucu tablo olarak görün.
    """)
    question = gr.Textbox(label="Soru", placeholder="Ör: 2020 yılında en çok sipariş veren kullanıcıları listele", lines=3)
    with gr.Row():
        run_btn = gr.Button("txt to sql", variant="primary")
        random_btn = gr.Button("Rastgele Soru Üret (Gemini)")
    sql_out = gr.Textbox(label="Oluşan SQL Sorgusu", lines=3, interactive=False)
    table_out = gr.Dataframe(label="Sorgu Sonucu Tablo", interactive=False)
    run_btn.click(fn=gradio_akisi, inputs=question, outputs=[sql_out, table_out])
    question.submit(fn=gradio_akisi, inputs=question, outputs=[sql_out, table_out])
    random_btn.click(fn=gemini_soru_uret, inputs=None, outputs=question)

demo.launch(share=True)

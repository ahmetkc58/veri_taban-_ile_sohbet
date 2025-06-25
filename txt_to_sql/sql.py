import pyodbc
import pandas as pd
from tabulate import tabulate
import warnings

warnings.filterwarnings("ignore", message="pandas only supports SQLAlchemy connectable*")

def sql_sorgusu_calistir(sorgu, dsn="DESKTOP-R738L1R", database="SatisVeritabani", return_df=False):
    """
    Verilen sorguyu MSSQL'de çalıştırır. return_df=True ise sonucu DataFrame olarak döndürür, aksi halde tablo olarak ekrana yazar.
    """
    if not sorgu.strip():
        print("Uyarı: Boş SQL sorgusu üretildi. Sorgu çalıştırılmadı.")
        return None if return_df else None
    print("\nOluşan SQL Sorgusu:\n", sorgu, "\n")
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={dsn};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
    )
    conn = pyodbc.connect(conn_str)
    df = pd.read_sql_query(sorgu, conn)
    conn.close()
    if return_df:
        return df
    if df.empty:
        print("Sonuç bulunamadı.")
    else:
        print(tabulate(df.head(20), headers='keys', tablefmt='grid', showindex=False))

# Artık ana akış main.py'de, bu dosya sadece fonksiyon sağlar.
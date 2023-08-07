import pandas as pd
import pickle
import json
from Code.model import MultinomialNaiveBayes
from Code.preprocess_text import preprocess_data
from Code.Cvec import CVec_transfrom

# =============================================
# Load Data tensi_skripsi
# =============================================
datajson= "./Dataset/Tensi_skripsi.json"
with open(datajson, 'r') as file:
        data = json.load(file)

# =============================================
# Read dile data preprocesing dan data X
# =============================================

with open('savemodel/data_prep.csv', 'r') as f: # Data Prep
      df = pd.read_csv(f)
      
with open('savemodel/X.csv', 'r') as f: # Data X
      X = pd.read_csv(f)
      
# =============================================
# Load data CVec.pkl
# =============================================
with open('./savemodel/CVec.pkl', 'rb') as f:
    CVec = pickle.load(f)

# =============================================
# model multinomial naive bayes
# =============================================
model = MultinomialNaiveBayes()

# membuat varabel "y" yang berisikan kategori dari data
y = df['kategori']

# ==============================================
# Melatih Model
# ==============================================
model.fit(X, y)

# ==============================================
# menerima inputan dan memberikan respon 
# berdasarkan model yang telah dilatih
# ==============================================
def get_response(question):
    
    # Melakukan preprocessing pada input yang akan diuji
    test = preprocess_data(question)
    
    # Mengubah input yang akan diuji menjadi bentuk yang dapat digunakan oleh algoritma Multinomial Naive Bayes
    test1 = CVec_transfrom(pd.Series([test]), CVec)

    # Mengklasifikasikan input berdasarkan model yang telah dibuat
    prediction = model.predict(test1.values)

    # Mengambil hasil klasifikasi (kelas prediksi)
    predicted_class = prediction[0]
    
    # Mendapatkan jawaban dari DataFrame berdasarkan kelas prediksi
    # Cari jawaban yang sesuai berdasarkan hasil prediksi kategori
    output_jawaban = "Kategori jawaban tidak ditemukan."
    if question == "#TD":
        output_jawaban = "Tekanan Darah"
    else:
        for item in data:
            if item["kategori"] == predicted_class:
                output_jawaban = item["jawaban"]
                break
    return output_jawaban
        
# # Contoh penggunaan chatbot
# input_question = "hipertensi itu apa?"
# response = get_response(input_question)
# print("Chatbot: ", response)
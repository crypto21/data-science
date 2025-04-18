
# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

### Latar Belakang
Jaya Jaya Institut adalah institusi pendidikan tinggi yang menghadapi masalah tingkat dropout siswa yang tinggi. Hal ini berdampak pada reputasi dan efektivitas sistem pembelajaran. Oleh karena itu, proyek ini bertujuan membangun sistem prediktif untuk mendeteksi potensi dropout sejak dini.

### Permasalahan Bisnis
Bagaimana cara mengidentifikasi siswa berisiko tinggi mengalami dropout berdasarkan data akademik dan karakteristik demografis?

### Cakupan Proyek
- Eksplorasi dan analisis data akademik siswa.
- Pembuatan model klasifikasi untuk memprediksi risiko dropout.
- Visualisasi data dalam bentuk dashboard interaktif.
- Rekomendasi tindakan berbasis data.

## Sumber Data

Dataset yang digunakan dalam proyek ini adalah Students Performance, yang tersedia di:
[https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

## Setup Environment

Ikuti langkah-langkah berikut untuk menjalankan proyek ini:

1. **Buat virtual environment (opsional tapi disarankan)**
   ```bash
   python -m venv venv
   source venv/bin/activate      # di Linux/Mac
   venv\Scripts\activate       # di Windows
   ```

2. **Install dependensi**
   Jika tersedia `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Jalankan Notebook**
   Buka Jupyter Notebook:
   ```bash
   jupyter notebook notebook.ipynb
   ```

4. **Lihat Dashboard**
   Dashboard interaktif dapat diakses melalui:
   [https://lookerstudio.google.com/reporting/4f8f0cb4-478e-42b8-8f8c-0e8bfcffcd33/page/njYEF](https://lookerstudio.google.com/reporting/4f8f0cb4-478e-42b8-8f8c-0e8bfcffcd33/page/njYEF)

## Data Understanding
Dataset terdiri dari 4424 entri dan 37 kolom. Target utama adalah kolom `Status` yang diklasifikasikan ulang menjadi `Dropout` (1) dan lainnya (0). Terdapat fitur numerik dan kategorikal yang beragam, seperti nilai akademik, jenis kelamin, usia masuk, beasiswa, dll.

## Data Preparation
- Encoding target `Dropout`
- Normalisasi fitur numerik
- Pembagian data train/test (80:20)
- Tidak ada missing value

## Modeling
Model yang digunakan: Random Forest

Hasil evaluasi:
- Akurasi: 89%
- Precision kelas dropout: 90%
- Recall kelas dropout: 73%
- F1-score kelas dropout: 80%

Model dan scaler disimpan di folder `model/` sebagai `.pkl`.

## Business Dashboard
Dashboard dibuat menggunakan Google Looker Studio untuk memvisualisasikan profil siswa dan korelasinya terhadap dropout. 
[https://lookerstudio.google.com/reporting/4f8f0cb4-478e-42b8-8f8c-0e8bfcffcd33/page/njYEF](https://lookerstudio.google.com/reporting/4f8f0cb4-478e-42b8-8f8c-0e8bfcffcd33/page/njYEF)

## Menjalankan Sistem Machine Learning
Sistem prediksi risiko dropout dapat dijalankan menggunakan file `app.py` berbasis Streamlit.

```bash
streamlit run app.py
```

Akses aplikasi pada link Streamlit Cloud berikut.
[https://data-science-etm85sk3knv5fmmjbyhe8x.streamlit.app/](https://data-science-etm85sk3knv5fmmjbyhe8x.streamlit.app/)

## Conclusion
Berdasarkan hasil analisis data dan model machine learning yang telah dibangun, ditemukan bahwa karakteristik umum siswa yang dropout di Jaya Jaya Institut antara lain:
- Jenis kelamin: Lebih banyak terjadi pada siswa laki-laki dibanding perempuan.
- Status beasiswa: Siswa yang tidak menerima beasiswa memiliki kecenderungan dropout yang lebih tinggi.
- Rata-rata nilai penerimaan: Siswa yang dropout umumnya memiliki nilai awal penerimaan yang lebih rendah dibanding siswa yang bertahan.
- Status pekerjaan orang tua: Banyak siswa dropout berasal dari latar belakang keluarga dengan orang tua yang tidak bekerja tetap.
- Lokasi tempat tinggal: Siswa yang tinggal jauh dari kampus atau di luar kota cenderung memiliki tingkat dropout lebih tinggi.
- Frekuensi ketidakhadiran: Tingkat absensi tinggi merupakan indikator kuat bahwa siswa tersebut memiliki risiko dropout.

Model machine learning yang dikembangkan berhasil mengidentifikasi pola tersebut dengan akurasi yang cukup baik, dan dapat digunakan sebagai dasar untuk strategi intervensi dini terhadap siswa berisiko.

Dengan mengetahui karakteristik ini, Jaya Jaya Institut diharapkan dapat merancang program pendampingan dan bantuan finansial yang lebih tepat sasaran untuk menekan angka dropout.

### Rekomendasi Action Items
- Memberikan bimbingan akademik atau konseling lebih awal pada siswa berisiko.
- Mengembangkan program dukungan finansial dan beasiswa untuk mencegah dropout.
- Menyempurnakan sistem pendaftaran dan orientasi untuk membantu adaptasi awal siswa.


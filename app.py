
import streamlit as st
import joblib
import numpy as np

# Load model dan scaler
try:
    model = joblib.load("model/dropout_model.pkl")
    scaler = joblib.load("model/scaler.pkl")
except FileNotFoundError:
    st.error("Model atau scaler tidak ditemukan. Pastikan file tersedia di folder 'model'.")
    st.stop()

st.title("Prediksi Risiko Dropout Mahasiswa")

features = [
    'Marital_status', 'Application_mode', 'Application_order', 'Course',
    'Daytime_evening_attendance', 'Previous_qualification', 'Previous_qualification_grade',
    'Nacionality', 'Mothers_qualification', 'Fathers_qualification',
    'Mothers_occupation', 'Fathers_occupation', 'Admission_grade',
    'Displaced', 'Educational_special_needs', 'Debtor', 'Tuition_fees_up_to_date',
    'Gender', 'Scholarship_holder', 'Age_at_enrollment', 'International',
    'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_without_evaluations',
    'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_without_evaluations',
    'Unemployment_rate', 'Inflation_rate', 'GDP'
]

user_input = []
st.subheader("Masukkan Nilai Fitur:")
for feat in features:
    val = st.number_input(f"{feat}", value=0.0, format="%.2f")
    user_input.append(val)

if st.button("Prediksi"):
    try:
        X = np.array(user_input).reshape(1, -1)
        X_scaled = scaler.transform(X)
        result = model.predict(X_scaled)[0]
        st.success("Prediksi: " + ("💥 Berisiko Dropout" if result == 1 else "✅ Tidak Dropout"))
    except ValueError as e:
        st.error(f"Terjadi kesalahan dalam prediksi: {e}")
    except Exception as e:
        st.error(f"Kesalahan tidak terduga: {e}")

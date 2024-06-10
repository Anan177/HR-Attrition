import pandas as pd
from sklearn.preprocessing import StandardScaler
from joblib import load
import os

new_directory = input('Masukan direktori kerja:')

# Mengubah direktori kerja saat ini
os.chdir(new_directory)

# Memeriksa apakah direktori kerja sudah diubah
current_directory = os.getcwd()
print("Direktori saat ini:", current_directory)


Nominal_category = ['BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime']

logistic_regression_model = load('Attrition_logistic_regression_model.joblib')
svm_model = load('Attrition_svm_model.joblib')
random_forest_model = load('Attrition_randomforest.joblib')

scaler = load('scaler.pkl')

def preprocess_data(df):
    df.drop(columns=['EmployeeId','EmployeeCount', 'Over18', 'StandardHours', 'Attrition'], inplace=True)
    X_encoded = pd.get_dummies(df, columns=Nominal_category, dtype=int)
    X_scaled = scaler.transform(X_encoded)
    return X_scaled

def predict_with_models(X):
    prediction_logistic = logistic_regression_model.predict(X)
    prediction_svm = svm_model.predict(X)
    prediction_random_forest = random_forest_model.predict(X)
    return prediction_logistic, prediction_svm, prediction_random_forest

# Load new data
new_data_file = input("Masukkan nama file data baru: ")  # Meminta input nama file dari pengguna
new_data = pd.read_csv(new_data_file)

# Mengubah direktori kerja saat ini
os.chdir(new_directory)

# Memeriksa apakah direktori kerja sudah diubah
current_directory = os.getcwd()
print("Direktori saat ini:", current_directory)

model_num = int(input("Pilih model yang ingin digunakan:\n1. LogisticRegression\n2. SVM\n3. RandomForest\nNomor Model: "))

# Preprocess new data
X_new = preprocess_data(new_data)

prediction_logistic, prediction_svm, prediction_random_forest = predict_with_models(X_new)

if model_num == 1:
    print("Prediction Logistic:\n", prediction_logistic)
elif model_num == 2:
    print("Prediction SVM:\n", prediction_svm)
elif model_num == 3:
    print("Prediction RandomForest:\n", prediction_random_forest)
else:
    print("Nomor model salah, masukkan nomor model yang tepat")

df_pred = pd.DataFrame({
    'Attrition_prediksi': prediction_logistic if model_num == 1 else (prediction_svm if model_num == 2 else prediction_random_forest)
})

# Menyimpan DataFrame ke dalam file CSV
df_pred.to_csv('hasil_prediksi.csv', index=False)

print("Hasil prediksi telah disimpan dalam file hasil_prediksi.csv")

# 🔐 SecureLife Insurance Premium Estimator

Welcome to the **SecureLife Insurance Premium Predictor App**!

This project helps SecureLife agents and customers estimate insurance premiums based on personal lifestyle, financial, and policy information — all through a machine learning-powered web app.

> *Data-driven insights to protect what matters most.*

---

## 📸 App Preview

![App Screenshot](https://raw.githubusercontent.com/PaskidoNazzTech/Capstone_Insurance_Predictor/master/images/app_preview.png)

🔗 [Try the App](https://securelifeinsurance.streamlit.app/)

---

## 📌 Project Overview

- **🎓 Project Title:** Predicting Insurance Premiums with Data-Driven Insights for SecureLife Insurance Co.  
- **👤 Submitted by:** Emmanuel Obiorah  
- **🏛️ Program:** 3MTT Data Science Cohort 3  
- **📅 Timeline:** 7-week Capstone Project

---

## 🎯 Objective

To develop and deploy a regression model that predicts customer insurance premiums using a trained **Random Forest Regressor**, and deploy it through an interactive **Streamlit web app**.

---

## 🧠 Features

This app predicts insurance premiums based on:
- Age  
- Annual Income  
- Health Score  
- Credit Score  
- Number of Dependents  
- Policy Age  
- Vehicle Age  
- Insurance Duration  
- Number of Previous Claims

---

## 🛠️ Tech Stack

| Category       | Tools Used                                  |
|----------------|----------------------------------------------|
| Programming    | Python, Jupyter, Streamlit                   |
| Modeling       | Random Forest Regressor (scikit-learn)       |
| Visualization  | Matplotlib, Seaborn                          |
| Version Control| Git, GitHub                                  |
| Deployment     | Streamlit Cloud                              |
| Environments   | VSCode, Google Colab                         |

---

## 🧪 Project Structure

```
Capstone_Insurance_Predictor/
│
├── Capstone1_EDA_Preprocessing_EmmanuelObiorah.ipynb
├── Capstone1_Modeling_EmmanuelObiorah.ipynb
├── Capstone1_Tuning_EmmanuelObiorah.ipynb
├── Capstone1_Streamlit_EmmanuelObiorah.ipynb
├── Capstone1_Streamlit_EmmanuelObiorah.py
│
├── encoded_insurance_data.csv
├── best_rf_model.pkl
├── requirements.txt
├── README.md
```

---

## 🚀 How to Run the App Locally

1. **Clone the repository**  
   ```bash
   git clone https://github.com/PaskidoNazzTech/Capstone_Insurance_Predictor.git
   cd Capstone_Insurance_Predictor
   ```

2. **Create virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**  
   ```bash
   streamlit run Capstone1_Streamlit_EmmanuelObiorah.py
   ```

---

## 💡 Key Insights

- **Health Score, Age, and Credit Score** are strong premium drivers.
- **Policy Type and Smoking Status** significantly influence pricing.
- Categorical analysis validated realistic insurance logic.
- Model achieved **R² = 0.92**, **MAE ≈ ₦4,125**, **RMSE ≈ ₦6,898**.

---

## 🧩 Challenges Faced

- 🔧 File size limit errors while pushing to GitHub ➝ Solved using **Git LFS**
- ⚙️ Debugging Streamlit model loading issues ➝ Fixed with proper path handling
- 🔄 Switching between VSCode and Colab environments ➝ Managed via `.gitignore` and requirements syncing

> **“Every real project involves unexpected roadblocks — learning to resolve them is part of the journey.”**

---

## 📬 Contact

**Emmanuel Obiorah**  
GitHub: [@PaskidoNazzTech](https://github.com/PaskidoNazzTech)  
Email: jarmmax15@gmail.com

---

## 🏁 Final Note

This capstone project represents a complete lifecycle of a real-world machine learning solution — from raw data to deployment. It reflects technical, analytical, and problem-solving skills built during the 3MTT Data Science program.

---

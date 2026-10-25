# 🏥 Health Insurance Cost Predictor

A Machine Learning web application built with **Python and Streamlit** that predicts the estimated annual health insurance premium based on personal, demographic, and lifestyle information.

The application uses a trained Machine Learning model saved with **Joblib** and provides an easy-to-use web interface for making predictions.

---

## 🚀 Features

- 👤 Age-based insurance prediction
- ⚧️ Male/Female selection
- ⚖️ BMI input
- 👶 Children/Dependents information
- 🚬 Smoker/Non-Smoker selection
- 🌎 Region selection
- 💰 Estimated annual insurance premium
- 📊 Clean and interactive Streamlit interface
- ⚡ Cached model loading using `st.cache_resource`

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Streamlit**
- **Joblib**
- **Machine Learning**

---

## 📂 Project Structure

```text
Health_Insurance_Cost_Prediction/
│
├── health_insurance.py
├── model_joblib_gr
├── requirements.txt
└── README.md
```

---

## 📋 Input Features

The model uses the following features for prediction:

| Feature | Description |
|---|---|
| `age` | Age of the person |
| `sex` | Gender of the person |
| `bmi` | Body Mass Index |
| `children` | Number of children/dependents |
| `smoker` | Smoking status |
| `region` | Residential region |

### Region Mapping

| Region | Value |
|---|---:|
| Southwest | 1 |
| Southeast | 2 |
| Northwest | 3 |
| Northeast | 4 |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Health_Insurance_Cost_Prediction.git
```

Move into the project directory:

```bash
cd Health_Insurance_Cost_Prediction
```

---

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

---

### 3. Activate Virtual Environment

#### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell gives an execution-policy error, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

#### Windows CMD

```cmd
.venv\Scripts\activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet, install the required packages manually:

```bash
pip install streamlit joblib pandas
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run health_insurance.py
```

The application will open in your browser.

Usually, Streamlit runs at:

```text
http://localhost:8501
```

---

## 🧠 How It Works

The application follows these steps:

```text
User Input
    ↓
Streamlit Interface
    ↓
Convert Input into Pandas DataFrame
    ↓
Load Trained ML Model
    ↓
Model Prediction
    ↓
Display Estimated Insurance Premium
```

The user enters:

- Age
- Gender
- BMI
- Number of dependents
- Smoking status
- Region

These values are converted into a Pandas DataFrame with the required feature names:

```python
columns=["age", "sex", "bmi", "children", "smoker", "region"]
```

The trained model then predicts the estimated annual insurance cost.

---

## 💻 Example

For example, a user may enter:

```text
Age: 25
Sex: Male
BMI: 25.0
Children: 0
Smoker: No
Region: Southwest
```

The application processes these values and displays the predicted annual insurance premium.

---

## 📦 Model

The trained Machine Learning model is stored in:

```text
model_joblib_gr
```

The application loads the model using Joblib:

```python
model = joblib.load("model_joblib_gr")
```

The model is cached using Streamlit's `st.cache_resource` so that it does not need to be loaded again on every interaction.

---

## 🌐 Deployment

This Streamlit application can be deployed using platforms such as:

- Streamlit Community Cloud
- Render
- Other Python-compatible hosting platforms

For Streamlit Community Cloud, connect your GitHub repository and select:

```text
Main file: health_insurance.py
```

Then deploy the application.

---

## 📌 Important

Make sure the trained model file is available in the same project directory:

```text
model_joblib_gr
```

Otherwise, the application will not be able to load the model.

---

## ⚠️ Disclaimer

This project provides an **estimated insurance premium based on a Machine Learning model and historical data**. It is intended for educational and demonstration purposes and should not be considered an actual insurance quote.

---

## 👨‍💻 Author

**Vaghani Jil**

---

## ⭐ If You Like This Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

# 🎓 AI-Powered Student Support Chatbot using Machine Learning

An AI-powered Student Support Chatbot developed using **Python**, **Flask**, and **Machine Learning**. The chatbot classifies student queries using the **TF-IDF Vectorizer** and **Multinomial Naive Bayes** algorithm, then returns relevant responses for common student services.

---

## 📌 Features

- Student-friendly chatbot interface
- Machine Learning based text classification
- TF-IDF Vectorizer for text preprocessing
- Multinomial Naive Bayes classifier
- Fast and lightweight Flask backend
- Supports common student queries:
  - Admissions
  - Fees
  - Courses
  - Hostel
  - Placements
  - Scholarships
  - Library
  - Faculty
  - Examinations

---

## 🛠 Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Multinomial Naive Bayes

---

## 📂 Project Structure

```
AI-Powered-Student-Support-Chatbot-ML/
│
├── app.py
├── train_model.py
├── dataset.csv
├── chatbot_model.pkl
├── vectorizer.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Powered-Student-Support-Chatbot-ML.git
```

### 2. Navigate to the project folder

```bash
cd AI-Powered-Student-Support-Chatbot-ML
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Machine Learning model

```bash
python train_model.py
```

### 5. Run the Flask application

```bash
python app.py
```

### 6. Open your browser

```
http://127.0.0.1:5000
```

---

## 🤖 Machine Learning Workflow

```
Student Question
        │
        ▼
TF-IDF Vectorizer
        │
        ▼
Multinomial Naive Bayes
        │
        ▼
Predict Query Category
        │
        ▼
Return Appropriate Response
```

---

## 📊 Dataset

The chatbot is trained using a custom dataset containing student-related questions categorized into:

- Admission
- Fees
- Hostel
- Courses
- Placement
- Scholarship
- Faculty
- Library
- Examination

---

## 📸 Screenshots

Add screenshots of your chatbot interface here after running the project.

---

## 🚀 Future Improvements

- Database integration
- Voice-based interaction
- Multi-language support
- User authentication
- Integration with Large Language Models (LLMs)
- Real-time college information

---

## 👨‍💻 Author

**Vansh**

B.Tech Computer Science Engineering

---

## 📄 License

This project is licensed under the MIT License.

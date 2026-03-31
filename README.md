# 🥗 NutriScan AI

An AI-powered web application that analyzes food images and provides detailed nutritional information including calories, macronutrients, ingredients, and health advice — all in seconds.

---

## 📌 About the Project

NutriScan AI is a college project built for the subject **Artificial Intelligence**. The application allows users to upload an image of any food item and instantly receive a comprehensive nutritional breakdown powered by the **Groq API**. The goal is to make healthy eating more accessible by giving users quick insights into what they're consuming.

---

## ✨ Features

- 📷 **Food Image Upload** — Upload any food image directly through the web interface
- 🍎 **Food Item & Ingredient Detection** — Identifies the food and its likely ingredients
- 🔥 **Calorie Estimation** — Provides an estimated calorie count for the detected food
- 💪 **Macronutrient Breakdown** — Displays protein, carbohydrates, and fat content
- 🏥 **Health Score & Diet Advice** — Gives a health rating and personalized dietary suggestions
- ⚡ **Fast AI Inference** — Powered by Groq API for ultra-fast responses

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web UI framework |
| Groq API | AI model inference for food analysis |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or above
- A valid [Groq API Key](https://console.groq.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/nutrition-detector-ai.git
   cd nutrition-detector-ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Groq API Key**

   Create a `.env` file in the root directory and add:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. Open your browser and go to `http://localhost:8501`

---

## 📸 How to Use

1. Launch the app using the command above
2. Upload an image of any food item
3. Click the **Analyze** button
4. View the detailed nutritional breakdown and health advice

---

## 📁 Project Structure

```
nutrition-detector-ai/
│
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env                 # API keys (not pushed to GitHub)
├── .gitignore           # Ignored files
└── README.md            # Project documentation
```

---

## ⚠️ Important Note

Never push your `.env` file or API key to GitHub. Make sure `.env` is listed in your `.gitignore` file.

---

## 👨‍💻 Author

- Ajeet Singh
- Roll No. 2419817 
- Branch CSE 4th Semester 
- College: Chandigarh Engineering College 
- Subject: Artificial Intelligence
- GitHub: [@Ajeet22222](https://github.com/Ajeet22222)

---

## 📄 License

This project is made for educational purposes as part of a college assignment.